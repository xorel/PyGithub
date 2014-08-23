# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import CodeGeneration.PythonSnippets as PS
from CodeGeneration.CaseUtils import toUpperCamel


# @todoAlpha Implement the following, rephrase it and put it in the "rationales" doc
# About Completability and Updatability
#  - this does not apply to the Github class
#  - all classes have a 'url' attribute (things that don't are structures)
#  - all classes are lazilly completable, even if there is no use case for this now (like AuthenticatedUser which is always returned fully) to be future-proof
#  - all classes are updatable (have a .update method), even if they represent immutable objects (like GitTag), and in that case, .update always returns False, but this keeps the interface consistent
#  - structures are updatable (have a ._updateAttributes method) iif they are (recursively) an attribute of a class. (This is currently not enforced, and instead specified manually in the .yml file)
# Examples of classes:
#   mutable     returned partially      examples
#   True        True                    User
#   True        False                   AuthenticatedUser
#   False       True                    GitCommit
#   False       False                   GitTag
# Examples of structures:
#   updatable   examples
#   True        AuthenticatedUser.Plan
#   False       Github.GitIgnoreTemplate

# CodeGeneration.CodeGenerator
# @todoAlpha remove special cases :-/

# CodeGeneration.RstGenerator
# @todoAlpha document the sha from developer.github.com
# @todoAlpha document how many end-points are implemented and unimplemented

# Global
# @todoAlpha test lazy completion of all classes?
# @todoAlpha What happens when a suspended enterprise user tries to do anything?


class CodeGenerator:
    def generateClass(self, klass):
        yield "import uritemplate"
        yield ""
        yield "import PyGithub.Blocking._base_github_object as _bgo"
        yield "import PyGithub.Blocking._send as _snd"
        yield "import PyGithub.Blocking._receive as _rcv"
        if klass.base is not None:
            yield ""
            yield "import {}".format(self.computeModuleNameFor(klass.base))
        yield ""
        yield ""

        if klass.base is None:
            if klass.qualifiedName == "Github":
                baseName = "_bgo.SessionedGithubObject"
            else:
                baseName = "_bgo.UpdatableGithubObject"
        else:
            baseName = self.computeFullyQualifiedName(klass.base)

        yield from (
            PS.Class(klass.simpleName)
            .base(baseName)
            .docstring(self.generateDocStringForClass(klass, baseName))
            .elements(self.createClassStructure(s) for s in klass.structures)
            .elements(self.createClassPrivateParts(klass))
            .elements(self.createClassProperty(a) for a in klass.attributes)
            .elements(
                [] if klass.qualifiedName == "Github" else [
                    PS.Property("url")
                    .docstring(":type: :class:`string`")
                    .body("return self._url")
                ]
            )
            .elements(self.createClassMethod(m) for m in klass.methods)
            .elements(
                [] if klass.qualifiedName == "Github" else [
                    PS.Method("update")
                    .docstring("Makes a `conditional request <http://developer.github.com/v3/#conditional-requests>`_ and updates the object.")
                    .docstring("Returns True if the object was updated.")
                    .docstring("")
                    .docstring(":rtype: :class:`bool`")
                    .body("return self._update()")
                ]
            )
        )

    def generateDocStringForClass(self, klass, baseName):
        yield "Base class: :class:`.{}`".format(baseName.split(".")[-1])
        yield ""
        if len(klass.derived) == 0:
            yield "Derived classes: none."
        else:
            yield "Derived classes:"
            for d in klass.derived:
                yield "  * :class:`.{}`".format(d.qualifiedName)
        yield ""
        yield from self.generateDocForSourcesAndSinks(klass)

    def generateDocForSourcesAndSinks(self, klass):
        assert len(klass.sources) != 0
        yield "Methods and attributes returning instances of this class:"
        for source in klass.sources:
            yield "  * {}".format(self.generateDocForSource(source))
        yield ""
        if len(klass.sinks) == 0:
            yield "Methods accepting instances of this class as parameter: none."
        else:
            yield "Methods accepting instances of this class as parameter:"
            for sink in klass.sinks:
                yield "  * {}".format(self.generateDocForSink(sink))

    def generateDocForSource(self, source):
        return self.getMethod("generateDocFor{}", source.__class__.__name__)(source)

    def generateDocForMethodSource(self, source):
        return ":meth:`.{}`".format(source.object.qualifiedName)

    def generateDocForAttributeSource(self, source):
        return ":attr:`.{}`".format(source.object.qualifiedName)

    def generateDocForSink(self, sink):
        return ":meth:`.{}`".format(sink.object.qualifiedName)

    def createClassStructure(self, structure):
        return (
            PS.Class(structure.simpleName)
            .base("_bgo.SessionedGithubObject")
            .docstring(self.generateDocForSourcesAndSinks(structure))
            .elements(self.createStructPrivateParts(structure))
            .elements(self.createStructProperty(a) for a in structure.attributes)
        )

    def createStructPrivateParts(self, structure):
        yield (  # pragma no cover
            PS.Method("_initAttributes")
            .parameters((a.simpleName, "None") for a in structure.attributes)
            .parameters((a, "None") for a in structure.deprecatedAttributes)
            .parameter("**kwds")
            .body(self.generateImportsForAllUnderlyingTypes(structure, [a.type for a in structure.attributes]))
            .body("super({}, self)._initAttributes(**kwds)".format(structure.qualifiedName))
            .body("self.__{} = {}".format(a.simpleName, self.createCallForAttributeInitializer(a)) for a in structure.attributes)
        )
        if structure.isUpdatable:
            yield(
                PS.Method("_updateAttributes")
                .parameters((a.simpleName, "None") for a in structure.attributes)
                .parameters((a, "None") for a in structure.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}, self)._updateAttributes(**kwds)".format(structure.qualifiedName))
                .body("self.__{0}.update({0})".format(a.simpleName) for a in structure.attributes)
            )

    def createStructProperty(self, attribute):
        return (
            PS.Property(attribute.simpleName)
            .docstring(":type: {}".format(self.generateDocForType(attribute.type)))
            .body("return self.__{}.value".format(attribute.simpleName))
        )

    def createClassPrivateParts(self, klass):
        if len(klass.attributes) != 0:
            yield (  # pragma no cover
                PS.Method("_initAttributes")
                .parameters((a.simpleName, "_rcv.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
                .body(self.generateImportsForAllUnderlyingTypes(klass, [a.type for a in klass.attributes]))
                .body("super({}, self)._initAttributes(**kwds)".format(klass.qualifiedName))
                .body("self.__{} = {}".format(a.simpleName, self.createCallForAttributeInitializer(a)) for a in klass.attributes)
            )
            yield (
                PS.Method("_updateAttributes")
                .parameter("eTag")
                .parameters((a.simpleName, "_rcv.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}, self)._updateAttributes(eTag, **kwds)".format(klass.qualifiedName))
                .body("self.__{0}.update({0})".format(a.simpleName) for a in klass.attributes)
            )

    def generateImportsForAllUnderlyingTypes(self, klass, types):
        imports = set()
        for type in types:
            for t in type.underlyingTypes:
                if t.__class__.__name__ == "Class" and t is not klass and t.qualifiedName not in ["PaginatedList", "SearchResult"]:
                    imports.add(self.computeModuleNameFor(t))
                if t.__class__.__name__ == "Structure" and klass.__class__.__name__ == "Class" and t.containerClass is not klass:
                    imports.add(self.computeModuleNameFor(t))
        for i in sorted(imports):
            yield "import {}".format(i)

    def createCallForAttributeInitializer(self, attribute):
        return (
            PS.Call("_rcv.Attribute")
            .arg('"{}"'.format(attribute.qualifiedName))
            .arg(self.generateCodeForConverter(attribute, attribute.type))
            .arg(attribute.simpleName)
        )

    def generateCodeForConverter(self, attribute, type):
        return "_rcv.{}".format(self.getMethod("generateCodeFor{}Converter", type.__class__.__name__)(attribute, type))

    def generateCodeForLinearCollectionConverter(self, attribute, type):
        return self.getMethod("generateCodeFor{}Converter", type.container.simpleName)(attribute, type)

    def generateCodeForListConverter(self, attribute, type):
        return "ListConverter({})".format(self.generateCodeForConverter(attribute, type.content))

    def generateCodeForMappingCollectionConverter(self, attribute, type):
        return "DictConverter({}, {})".format(self.generateCodeForConverter(attribute, type.key), self.generateCodeForConverter(attribute, type.value))

    def generateCodeForBuiltinTypeConverter(self, attribute, type):
        return "{}Converter".format(toUpperCamel(type.simpleName))

    def generateCodeForClassConverter(self, attribute, type):
        return "ClassConverter(self.Session, {})".format(self.computeContextualName(type, attribute))

    def generateCodeForUnionTypeConverter(self, attribute, type):
        assert type.key is not None
        converters = {k: self.generateCodeForConverter(attribute, t) for k, t in zip(type.keys, type.types)}
        return 'KeyedStructureUnionConverter("{}", dict({}))'.format(type.key, ", ".join("{}={}".format(k, v) for k, v in sorted(converters.items())))

    def generateCodeForStructureConverter(self, attribute, type):
        return "StructureConverter(self.Session, {})".format(self.computeContextualName(type, attribute))

    def createClassProperty(self, attribute):
        return (
            PS.Property(attribute.simpleName)
            .docstring(attribute.doc)
            .docstring(None if attribute.doc is None else "")
            .docstring(":type: {}".format(self.generateDocForType(attribute.type)))
            .body("self._completeLazily(self.__{}.needsLazyCompletion)".format(attribute.simpleName))
            .body("return self.__{}.value".format(attribute.simpleName))
        )

    def createClassMethod(self, method):
        return (
            PS.Method(method.simpleName)
            .parameters((p.name, "None") if p.optional else "*{}".format(p.name) if p.variable else p.name for p in method.parameters)
            .docstring(self.generateDocStringForMethod(method))
            .body(self.generateMethodBody(method))
        )

    def generateDocStringForMethod(self, method):
        # @todoSomeday Document the "or" aspect of a method calling several end-points
        for endPoint in method.endPoints:
            yield "Calls the `{} {} <{}>`__ end point.".format(endPoint.verb, endPoint.url, endPoint.doc)
            yield ""
            if len(endPoint.methods) > 1:
                yield "The following methods also call this end point:"
                for otherMethod in endPoint.methods:
                    if otherMethod is not method:
                        yield "  * :meth:`.{}`".format(otherMethod.qualifiedName)
            else:
                yield "This is the only method calling this end point."
            yield ""
        if method.doc is not None:
            yield method.doc
            yield ""
        for parameter in method.parameters:
            yield ":param {}: {} {}".format(
                parameter.name,
                "optional" if parameter.optional else "mandatory",
                self.generateDocForType(parameter.type)
            )
        yield ":rtype: {}".format(self.generateDocForType(method.returnType))

    def generateMethodBody(self, method):
        # @todoAlpha Maybe for special cases we should just call a function named after the method, but living in real code so that we can unit-test it.
        yield from self.generateImportsForAllUnderlyingTypes(method.containerClass, [method.returnType])
        yield ""
        if len(method.parameters) != 0:
            for p in method.parameters:
                if p.name == "files":  # @todoAlpha Remove this special case for AuthenticatedUser.create_gist when input type has been decided
                    pass
                elif p.name == "context":
                    yield "if context is not None:"
                    yield "    context = _snd.normalizeRepositoryFullNameBis(context)"
                elif p.name == "per_page":
                    yield "if per_page is None:"
                    yield "    per_page = self.Session.PerPage"
                    yield "else:"
                    yield "    per_page = _snd.normalizeInt(per_page)"
                elif method.qualifiedName == "Github.get_repo" and p.name == "repo":
                    yield "repo = _snd.normalizeTwoStringsString(repo)"
                elif p.name == "labels" and method.qualifiedName in ["Repository.get_issues", "AuthenticatedUser.get_issues", "AuthenticatedUser.get_user_issues", "Organization.get_issues"]:
                    yield "if {} is not None:".format(p.name)
                    yield '    labels = ",".join(_snd.normalizeList(_snd.normalizeLabelName, labels))'
                elif p.variable and p.name == "email":
                    yield "email = _snd.normalizeList(_snd.normalizeString, email)"
                elif p.variable and p.name == "label":
                    yield "label = _snd.normalizeList(_snd.normalizeLabelName, label)"
                elif p.optional:
                    yield "if {} is not None:".format(p.name)
                    yield from PS.indent(self.generateCodeToNormalizeParameter(p))
                else:
                    yield from self.generateCodeToNormalizeParameter(p)
            yield ""

        # @todoSomeday Open an issue to Github to make name optional in PATCH /repository
        if method.qualifiedName == "Repository.edit":
            yield "if name is None:"
            yield "    name = self.name"
            yield ""

        if method.qualifiedName == "Repository.get_git_ref":
            yield 'url = uritemplate.expand(self.git_refs_url) + "/" + ref'
        elif method.qualifiedName == "Issue.create_pull":
            yield 'url = "/".join(self._url.split("/")[:-2]) + "/pulls"'
        elif method.qualifiedName == "Commit.create_status":
            yield 'url = "/".join(self._url.split("/")[:-2]) + "/statuses/" + self.sha'
        elif method.qualifiedName == "Hook.test":
            yield 'url = self._url + "/tests"'
        elif method.qualifiedName == "Hook.ping":
            yield 'url = self._url + "/pings"'
        elif method.qualifiedName == "Commit.get_statuses":
            yield 'url = self._url + "/statuses"'
        # elif method.qualifiedName == "Commit.get_status":
        #     yield 'url = self._url + "/status"'
        elif method.qualifiedName == "GitTree.create_modified_copy":
            yield "url = self._url[:self._url.rfind(self.sha) - 1]"
        elif len(method.urlTemplateArguments) == 0:
            url = self.generateCodeForValue(method, method.urlTemplate)
            if method.urlTemplate.__class__.__name__ == "EndPointValue":
                yield "url = {}".format(url)
            else:
                yield "url = uritemplate.expand({})".format(url)
        else:
            yield "url = uritemplate.expand({}, {})".format(self.generateCodeForValue(method, method.urlTemplate), ", ".join("{}={}".format(a.name, self.generateCodeForStringValue(method, a.value)) for a in method.urlTemplateArguments))  # pragma no branch
        if len(method.urlArguments) != 0:
            yield "urlArguments = _snd.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.urlArguments))  # pragma no branch
        if len(method.postArguments) != 0:
            if method.qualifiedName in ["AuthenticatedUser.add_to_emails", "AuthenticatedUser.remove_from_emails"]:
                # @todoAlpha solve those special cases by changing Method.postArguments to Method.postPaylod, polymorphic, with DictionaryPayload and DirectPayload. Also change Session._request's parameter.
                yield "postArguments = email"
            elif method.qualifiedName in ["Issue.add_to_labels", "Issue.set_labels"]:
                yield "postArguments = label"
            elif method.qualifiedName == "Release.create_asset":
                yield "postArguments = content"
            else:
                yield "postArguments = _snd.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.postArguments))  # pragma no branch
        if len(method.headers) != 0:
            headers = ", ".join('"{}": {}'.format(a.name, self.generateCodeForValue(method, a.value)) for a in method.headers)
            yield "headers = {" + headers + "}"

        yield "r = self.Session._request{}({})".format("Anonymous" if method.qualifiedName == "Github.create_anonymous_gist" else "", self.generateCallArguments(method))  # @todoSomeday Remove hard-coded method name
        yield from self.generateCodeForEffects(method)
        if method.qualifiedName == "Repository.get_contents":
            yield "if isinstance(r.json(), dict):"
            yield '    return _rcv.KeyedUnion("type", dict(file=PyGithub.Blocking.File.File, submodule=PyGithub.Blocking.Submodule.Submodule, symlink=PyGithub.Blocking.SymLink.SymLink))(self.Session, r.json(), r.headers.get("ETag"))'
            yield "else:"
            yield "    return [_rcv.FileDirSubmoduleSymLinkUnion(PyGithub.Blocking.File.File, Repository.Dir, PyGithub.Blocking.Submodule.Submodule, PyGithub.Blocking.SymLink.SymLink)(self.Session, x) for x in r.json()]"
        elif method.qualifiedName in ["Github.get_users", "Repository.get_contributors"]:
            yield 'return _rcv.PaginatedList(_rcv.KeyedUnion("{}", dict({})), self.Session, r)'.format(method.returnType.content.key, ", ".join("{}={}".format(k, v) for k, v in sorted((k, self.computeContextualName(t, method)) for k, t in zip(method.returnType.content.keys, method.returnType.content.types))))
        else:
            yield from self.generateCodeForReturn(method)

    def generateCodeToNormalizeParameter(self, parameter):
        # @todoAlpha To solve the "variable parameter needs to be normalized as list" case, don't pass the parameter but its type, and return a format string where the caller will substitute the param name
        yield from self.getMethod("generateCodeToNormalize{}Parameter", parameter.type.__class__.__name__)(parameter)

    def generateCodeToNormalizeEnumeratedTypeParameter(self, parameter):
        yield "{} = _snd.normalizeEnum({}, {})".format(parameter.name, parameter.name, ", ".join('"' + v + '"' for v in parameter.type.values))  # pragma no branch

    def generateCodeToNormalizeAttributeTypeParameter(self, parameter):
        yield "{} = _snd.normalize{}{}({})".format(parameter.name, parameter.type.type.simpleName, toUpperCamel(parameter.type.attribute.simpleName), parameter.name)

    def generateCodeToNormalizeUnionTypeParameter(self, parameter):
        yield "{} = _snd.normalize{}({})".format(parameter.name, "".join(((toUpperCamel(t.type.simpleName) + toUpperCamel(t.attribute.simpleName)) if t.__class__.__name__ == "AttributeType" else toUpperCamel(t.simpleName)) for t in parameter.type.types), parameter.name)  # pragma no branch

    def generateCodeToNormalizeBuiltinTypeParameter(self, parameter):
        yield "{} = _snd.normalize{}({})".format(parameter.name, toUpperCamel(parameter.type.qualifiedName), parameter.name)

    def generateCodeToNormalizeLinearCollectionParameter(self, parameter):
        yield from self.getMethod("generateCodeToNormalize{}Of{}Parameter", parameter.type.container.simpleName, parameter.type.content.__class__.__name__)(parameter)

    def generateCodeToNormalizeListOfAttributeTypeParameter(self, parameter):
        yield "{} = _snd.normalizeList(_snd.normalize{}{}, {})".format(parameter.name, parameter.type.content.type.simpleName, toUpperCamel(parameter.type.content.attribute.simpleName), parameter.name)

    def generateCodeToNormalizeListOfBuiltinTypeParameter(self, parameter):
        yield "{} = _snd.normalizeList(_snd.normalize{}, {})".format(parameter.name, toUpperCamel(parameter.type.content.simpleName), parameter.name)

    def generateCodeForEffects(self, method):
        for effect in method.effects:
            yield from self.generateCodeForEffect(method, effect)

    def generateCodeForEffect(self, method, effect):
        if effect == "update":
            yield 'self._updateAttributes(r.headers.get("ETag"), **r.json())'
        elif effect == "update from json.content":
            yield 'self._updateAttributes(None, **(r.json()["content"]))'
        elif effect == "update_attr content from parameter content":
            yield "self.__content.update(content)"
        else:
            assert False  # pragma no cover

    def generateCodeForReturn(self, method):
        yield from self.getMethod("generateCodeForReturn{}", method.returnType.__class__.__name__)(method)

    def generateCodeForReturnNoneType(self, method):
        assert method.returnFrom is None
        return []

    def generateCodeForReturnUnionType(self, method):
        if method.qualifiedName in ["Repository.get_stats_commit_activity", "Repository.get_stats_contributors"]:
            yield "if r.status_code == 202:"
            yield "    return []"
            yield "elif r.status_code == 204:"
            yield "    return None"
            yield "else:"
            yield "    return [{}(self.Session, x) for x in r.json()]".format(self.computeContextualName(method.returnType.types[1].content, method))
        elif method.qualifiedName == "Repository.get_stats_code_frequency":
            yield "if r.status_code == 202:"
            yield "    return []"
            yield "elif r.status_code == 204:"
            yield "    return None"
            yield "else:"
            yield "    return r.json()"
        elif method.qualifiedName == "Repository.get_stats_punch_card":
            yield "if r.status_code == 204:"
            yield "    return None"
            yield "else:"
            yield "    return r.json()"
        elif method.qualifiedName == "Repository.get_stats_participation":
            yield "if r.status_code == 204:"
            yield "    return None"
            yield "else:"
            yield "    return {}(self.Session, r.json())".format(self.computeContextualName(method.returnType.types[1], method))
        else:
            assert False, method.qualifiedName

    def generateCodeForReturnBuiltinType(self, method):
        if method.returnFrom == "status":
            assert method.returnType.simpleName == "bool"
            yield "return r.status_code == 204"
        elif method.returnFrom == "text":
            assert method.returnType.simpleName == "string"
            yield "return r.text"
        else:
            assert False, method.returnFrom  # pragma no cover

    def generateCodeForReturnMappingCollection(self, method):
        assert method.returnFrom is None
        assert method.returnType.container.simpleName == "dict"
        assert method.returnType.key.simpleName == "string"
        assert method.returnType.value.simpleName in ["string", "int"]
        yield "return r.json()"

    def generateCodeForReturnStructure(self, method):
        assert method.returnFrom is None
        yield 'return {}(self.Session, r.json())'.format(self.computeContextualName(method.returnType, method))

    def generateCodeForReturnClass(self, method):
        if method.returnFrom is None:
            data = "r.json()"
        else:
            assert method.returnFrom == "json.commit"
            data = 'r.json()["commit"]'
        yield 'return {}(self.Session, {}, r.headers.get("ETag"))'.format(self.computeContextualName(method.returnType, method), data)

    def generateCodeForReturnLinearCollection(self, method):
        yield from self.getMethod("generateCodeForReturn{}Of{}", method.returnType.container.simpleName, method.returnType.content.__class__.__name__)(method)

    def generateCodeForReturnSearchResultOfClass(self, method):
        assert method.returnFrom is None
        yield 'return _rcv.SearchResult({}, self.Session, r)'.format(self.computeContextualName(method.returnType.content, method))

    def generateCodeForReturnPaginatedListOfClass(self, method):
        assert method.returnFrom is None
        yield 'return _rcv.PaginatedList({}, self.Session, r)'.format(self.computeContextualName(method.returnType.content, method))

    def generateCodeForReturnPaginatedListOfStructure(self, method):
        assert method.returnFrom is None
        yield 'return _rcv.PaginatedList({}, self.Session, r)'.format(self.computeContextualName(method.returnType.content, method))

    def generateCodeForReturnListOfClass(self, method):
        assert method.returnFrom is None
        yield 'return [{}(self.Session, x, None) for x in r.json()]'.format(self.computeContextualName(method.returnType.content, method))

    def generateCodeForReturnListOfStructure(self, method):
        assert method.returnFrom is None
        yield 'return [{}(self.Session, x) for x in r.json()]'.format(self.computeContextualName(method.returnType.content, method))

    def generateCodeForReturnListOfBuiltinType(self, method):
        assert method.returnFrom is None
        assert method.returnType.content.simpleName == "string"
        yield "return r.json()"

    def computeContextualName(self, type, context):
        if self.computeModuleNameFor(type) == self.computeModuleNameFor(context.containerClass):
            return type.qualifiedName
        else:
            return self.computeFullyQualifiedName(type)

    def generateCallArguments(self, m):
        args = '"{}", url'.format(m.endPoints[0].verb)
        if m.returnType.qualifiedName == "bool":
            args += ", accept404=True"
        if len(m.urlArguments) != 0:
            args += ", urlArguments=urlArguments"
        if len(m.postArguments) != 0:
            args += ", postArguments=postArguments"
        if len(m.headers) != 0:
            args += ", headers=headers"
        return args

    def generateDocForType(self, type):
        return self.getMethod("generateDocFor{}", type.__class__.__name__)(type)

    def generateDocForBuiltinType(self, type):
        return ":class:`{}`".format(type.qualifiedName)

    def generateDocForClass(self, type):
        if type.qualifiedName == "PaginatedList":
            return ":class:`.PaginatedList`"
        else:
            return ":class:`~.{0}.{0}`".format(type.qualifiedName)

    def generateDocForAttributeType(self, type):
        if type.attribute.qualifiedName == "Repository.full_name":
            return ":class:`~PyGithub.Blocking.Repository.Repository` or :class:`string` (its :attr:`~PyGithub.Blocking.Repository.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.User.login` or :attr:`.Organization.login` and its :attr:`~PyGithub.Blocking.Repository.Repository.name`)"
        else:
            return ":class:`~.{}` or :class:`{}` (its :attr:`~.{}`)".format(self.computeFullyQualifiedName(type.type), type.attribute.type.qualifiedName, self.computeFullyQualifiedName(type.attribute))

    def generateDocForEnumeratedType(self, type):
        return " or ".join('"' + v + '"' for v in type.values)

    def generateDocForLinearCollection(self, type):
        return "{} of {}".format(self.generateDocForType(type.container), self.generateDocForType(type.content))

    def generateDocForMappingCollection(self, type):
        return "{} of {} to {}".format(self.generateDocForType(type.container), self.generateDocForType(type.key), self.generateDocForType(type.value))

    def generateDocForNoneType(self, type):
        return "None"

    def generateDocForStructure(self, type):
        return ":class:`.{}`".format(type.qualifiedName)

    def generateDocForUnionType(self, type):
        return " or ".join(self.generateDocForType(st) for st in type.types)

    def generateCodeForValue(self, method, value):
        return self.getMethod("generateCodeFor{}", value.__class__.__name__)(method, value)

    def generateCodeForEndPointValue(self, method, value):
        return '"https://api.github.com{}"'.format(method.endPoints[0].urlTemplate)

    def generateCodeForAttributeValue(self, method, value):
        if value.attribute == "url":
            return "self._url"
        else:
            return "self.{}".format(value.attribute)

    def generateCodeForRepositoryNameValue(self, method, value):
        return "{}[1]".format(value.repository)

    def generateCodeForRepositoryOwnerValue(self, method, value):
        return "{}[0]".format(value.repository)

    def generateCodeForParameterValue(self, method, value):
        return value.parameter

    def generateCodeForStringValue(self, method, value):
        format = "{}"
        if value.__class__.__name__[:-5] == "Parameter":
            p = [p for p in method.parameters if p.name == value.parameter][0]
            if p.type.qualifiedName in ["int"]:
                format = "str({})"
        if value.__class__.__name__[:-5] == "Attribute":
            a = self.findAttribute(method.containerClass, value.attribute)
            if a is not None and a.type.qualifiedName in ["int"]:
                format = "str({})"
        return format.format(self.generateCodeForValue(method, value))

    def getMethod(self, scheme, *names):
        name = scheme.format(*(toUpperCamel(name) for name in names))
        return getattr(self, name)

    def findAttribute(self, t, n):
        for a in t.attributes:
            if a.simpleName == n:
                return a
        if t.base is not None:
            return self.findAttribute(t.base, n)  # pragma no cover

    def computeModuleNameFor(self, t):
        return self.getMethod("computeModuleNameFor{}", t.__class__.__name__)(t)

    def computeModuleNameForClass(self, t):
        return "PyGithub.Blocking.{}".format(t.simpleName)

    def computeModuleNameForStructure(self, t):
        return self.computeModuleNameFor(t.containerClass)

    def computeModuleNameForAttribute(self, a):
        return self.computeModuleNameFor(a.containerClass)

    def computeFullyQualifiedName(self, t):
        return "{}.{}".format(self.computeModuleNameFor(t), t.qualifiedName)
