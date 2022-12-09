# Versioning
!!! warning "Requirement"
    - External APIs **must** version if they introduce a breaking change. 
    - Internal APIs with over one consumer **must** version if they introduce a breaking change. 

!!! success "Guidance"
    - It is OPTIONAL to version when introducing a breaking change if it is an internal API with only one consumer **AND** if the consumer’s clients can be updated at the same time as the API. An example of this would be a web app that is pushed out to all clients vs. a mobile app where updates roll out more slowly.

## Breaking change definition
At a high level, a breaking change is any change to an API that would cause an error in a consuming application. The following are all examples of breaking changes:

- Removing an endpoint
- Renaming an endpoint’s path
- Removing an HTTP verb (GET, POST, and so on) for an endpoint
- Removing a property 
- Renaming a property
- Changing a properties-level or tier within an object’s hierarchy
- Making a mandatory property optional 
- Changing a property’s type 
- Changing a property’s format 
- Adding or removing values from an enum

## API versioning scheme
!!! warning "Requirement"
    - APIs **must** only use URI (non-header)-based major versioning.
    - APIs **must** provide a major version number in the URI path after the namespace and before any resources/operations.
    - The versioning scheme **must** start with the lowercase character `v` followed by an integer, the combination of which produces an ordinal number, e.g. `v0`, `v1`, `v2`.
    - APIs **must** NOT expose minor or patch version numbers in the URI path.
    - A minor API version **must** maintain backward compatibility with all previous minor versions within the same major version.
    - For non-major changes, providers **must** still update the minor or patch versions in the OAS documentation.

!!! success "Guidance"
    - Versioning **should** start at `v0`.
    - Versioning **may** start with another ordinal number if the API is being ported to Lighthouse.

*The major version after the namespace.*
```
https://api.va.gov/benefits/v0
```
*Resources or operations specific to the endpoints within the API then show up after the version number.*
```
https://api.va.gov/benefits/v0/claims
```

## Incrementing minor versions

!!! success "Guidance"
    - Creating a new OAS doc for each minor version can result in many files that are virtually the same. Make use of '[reference definitions](https://swagger.io/docs/specification/using-ref/)', `$ref`, to reduce duplication and share definitions across OAS docs.


As minor and patch version information is not in the URI path, minor changes only need to be documented in the OAS doc for the API.

*Before*

```yaml
info:
  title: Benefits API
  ...
  version: 1.0.0
```

*After*

```yaml
	
info:
  title: Benefits API
  ...
  version: 1.1.0
```

