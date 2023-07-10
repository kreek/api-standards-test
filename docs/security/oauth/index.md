# OAuth 2.0

OAuth 2.0 lets an API consumer get an access token on behalf of a user (through our authorization code flow or authorization code flow with proof key for code exchange) or system (through client credentials grant). The API will verify the access token and authorize the request.

If your API will use OAuth 2.0, you need to provide the following as part of onboarding:

- Supported scopes
- Intended audience (for identity providers)
- Token profile (defaults are provided below, but Lighthouse can change these if you need)
  - Token lifespan (default is 1 hour for users, 5 minutes for systems)
  - Offline access using refresh tokens (default is enabled for users)
  - Refresh token lifespan (default is 7 days for users)

Lighthouse uses this information to establish a dedicated OAuth server authorization for your API or set of related APIs and consumer documentation on the developer portal, if applicable.

The OAuth URLs will typically mirror your service URLs and will follow this format:

```url
https://sandbox-api.va.gov/oauth2/{service-name}/{system}/v1/*
```

Lighthouse will give you:

- OAuth 2.0/OpenID Connect (OIDC) issuer metadata ([See an example of OIDC issuer metadata](https://sandbox-api.va.gov/oauth2/health/v1/.well-known/openid-configuration)), which:
  - Defines a valid token issuer
  - Defines the token signing keys
  - Acts as a quick-start guide for consumers using OAuth 2.0/OIDC libraries (more information on building OAuth 2.0/OIDC applications is available on the Lighthouse Authorization page)
- A token-validation key

Consumers will register for access to your API and obtain OAuth credentials via the [developer portal](https://developer.va.gov/onboarding).

## OAS Security Examples

### Authorization Code Flow

Below is an example of Authorization Code Flow for the fictitious ‘Rx’ API. The security scheme is called `oAuth2AuthCode` and the flow is `authorizationCode`. The `authorizationUrl` field contains the authorization endpoint that will be used to obtain the authorization code from the authorization server. The `tokenUrl` field contains the endpoint that is used by the client to obtain an access token. All supported scopes should be listed under `scopes`.

```yaml
components: 
  securitySchemes:
    oAuth2AuthCode: # (1)
      type: oauth2
      description: This API uses OAuth 2 with the authorization code grant flow.
      flows:
        authorizationCode: # (2)
          authorizationUrl: https://api.va.gov/oauth2/authorization   
          tokenUrl: https://api.va.gov/oauth2/token
          scopes:
            prescription.read: Retrieve prescription data
...
```

1. `oAuth2AuthCode` is the name of the security scheme.
2. The type of flow set for this security scheme is Authorization Code Flow.

The `oAuth2AuthCode` security scheme is then used in the security section of the `/prescriptions` endpoint. This endpoint requires the scope
 `prescription.read` so it is listed below the security scheme.

```yaml
paths:
  /prescriptions:
    get:
      tags:
        - prescription
      summary: Returns a list of a veteran's prescriptions
      security: # (1)
        - oAuth2AuthCode:
          - prescription.read # (2)
...                   
```

1. The `oAuth2AuthCode` security scheme is applied to this endpoint.
2. This endpoint requires the `prescription.read` scope.

### Client Credentials Grant

This example shows Client Credentials Grant being used in the ‘Rx’ API. The security scheme is called `oAuth2ClientCredentials` and the flow is `clientCredentials`. The `tokenUrl` field contains the endpoint that is used by the client to obtain an access token. All supported scopes should be listed under `scopes`.

```yaml
components: 
  securitySchemes:
    oAuth2ClientCredentials: # (1)
      type: oauth2
      description: This API uses OAuth 2 with the client credentials grant flow.
      flows:
        clientCredentials: # (2)
          tokenUrl: https://api.va.gov/oauth2/token
          scopes:
            prescription.read: Retrieve prescription data 
...
```

1. `oAuth2ClientCredentials` is the name of the security scheme.
2. The type of flow set for this security scheme is Client Credentials Grant.

The `oAuth2ClientCredentials` security scheme is used in the security section of the `/prescriptions` endpoint. This endpoint requires the scope `prescription.read` so it is listed below the security scheme.

```yaml
paths:
  /prescriptions:
    get:
      tags:
        - prescription
      summary: Returns a list of a veteran's prescriptions
      security: # (1)
        - oAuth2ClientCredentials:
          - prescription.read # (2)
...   
```

1. The `oAuth2ClientCredentials` security scheme is applied to this endpoint.
2. This endpoint requires the `prescription.read` scope.
