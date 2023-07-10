# API key

APIs that don't involve user authentication, PII, or PHI can use API keys for access control. Otherwise, your API will use [OAuth 2.0](oauth/index.md).

External consumers will register for access to an API and obtain an API key via the [developer portal](https://developer.va.gov/apply).

API keys are passed in using a request header and validated at the gateway. An API will not receive a request through the gateway without having a valid API key.

You can identify the consumer using the `X-Consumer-Username` header in the request.

!!! warning "Requirement"
    - Lighthouse does not apply resource or role-based access control with API keys. Your API is responsible for any fine-grained authorization.

## OAS Security Example

The example below defines an API key named `apiKey` that is sent as a request header. The security scheme is named `apiKeyAuth` and is used in the security section to apply the `apiKeyAuth` security scheme to the API. The `security` section shown below will apply the API key globally to all endpoints. Click on the circular buttons labeled with a '+' to view code annotations.

```yaml
components: 
  securitySchemes:
    apiKeyAuth: # (1)
      type: apiKey
      name: apiKey # (2)
      in: header

security: # (3)
  - apiKeyAuth: []
```

1. `apiKeyAuth` is the name of the security scheme.
2. `apiKey`is the name of the request header.
3. Security is set globally so the security scheme `apiKeyAuth` will apply to all endpoints.

The `apiKeyAuth` security scheme can also be applied to the operation level. Below, the `apiKeyAuth` security scheme is used in the security section of the `/pharmacies` endpoint. This is useful if only some endpoints need the API key.

```yaml
paths: 
  /pharmacies:
    get:
      tags:
        - pharmacy
      summary: Returns a list of facilities with pharmacies.
      description: Returns a paginated list of all VA facilities that provide pharmacological services.
      operationId: getPharmacies
      security: # (1)
        - apiKeyAuth: []
      responses:
        '200':
          description: The veteran's prescriptions were successfully found and returned as an array.
...
```

1. The `apiKeyAuth` security scheme is applied to this endpoint.
