# API Splitting

!!! warning "Requirement"
    - The parent API being split up **must** follow our [deprecation](/lifecycle/deprecation/) rules
    - The child APIs that have been split out are functionally new and **must** restart their versions at `v0`.

Over time an API may grow large enough or have taken on functionality where it makes sense to refactor into it multiple APIs.
Once the original API has been split, the resulting APIs are functionally new and must meet our standards as if they were freshly onboarding.

## Communication
API providers should warn consumers of the impending split before the new APIs are launched. Much of this communication will be through traditional channels (email, slack, etc.). Still, the API can communicate dates and links to more detailed information through `Deprecation` and `Link` HTTP headers.

```
Deprecation: Thu, 11 Nov 2048 23:59:59 UTC
Link: <https://developer.va.gov/deprecation/health#rx>; rel="deprecation"; type="text/html"
```

