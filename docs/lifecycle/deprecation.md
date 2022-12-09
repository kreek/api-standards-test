# Deprecation
As the API evolves, a need may arise to deprecate an API version, an API endpoint or a field in the API. The goal of deprecation is to progress to a state in which there are no consumers using the deprecated element. 

Getting to this state depends on clear, timely, and detailed documentation, communication, and monitoring.

!!! warning "Requirement"
    - Providers **must** [document](#documenting-deprecations) deprecated endpoints, or endpoints with deprecated elements in the OAS.
    - Providers **must** return [deprecation and an optional sunset header](#headers) in deprecated endpoint's responses.
    - Deprecated API endpoints and elements **must** remain supported for the life of the major version.

!!! success "Guidance"
    - Providers **should** define a sunset period for the feature they are deprecating. This period is up to the provider, but we recommend 3-12 months.
    - Providers **should** have a plan for communicating the deprecation and the sunset period to **all consumers** of the API.
    - Providers **should** monitor the deprecated API element to ensure its use is declining over the sunset period.


## Documenting deprecations
OAS uses a `deprecated` field to mark either complete endpoints or their specific elements as deprecated.
### HTTP methods
```yaml
paths:
  /appeals:
    get:
      description: Deprecated endpoint to retrieve appeals
      deprecated: true
```
### Query parameters
```yaml
paths:
  /appeals:
    get:
      description: Retrieve appeals status
      parameters:
        - name: fromDate
          in: query
          description: Deprecated start date of appeal
          deprecated: true
```
### Headers
```yaml
paths:
  /appeals:
    get:
      description: Retrieve appeals status
      parameters:
        - name: ORG-Authorization-Token
          in: header
          description: Deprecated ORG-Authorization-Token header
          deprecated: true
```
### Properties in a resource
```yaml
paths:
  /appeals:
    get:
      description: Retrieve appeals status
      responses:
        200:
          description: Successful appeal
          content:
            application/json:
              schema:
                $ref: “#/components/schemas/Appeal”
components:
  schemas:
    Appeal:
      description: Appeal status schema
      properties:
        appealType:
          type: string
          description: The decision review option chosen by the appellant
          deprecated: true
```

## Headers
The Internet Engineering Task Force has specified two headers for deprecation. ‘Deprecation’ and ‘Sunset’. Both headers seem similar, and that the Deprecation header can take a boolean true value or a timestamp can cause further confusion.
### Deprecation header
If deprecation starts at a future date, use an HTTP-date timestamp.
```
Deprecation: Thu, 11 Nov 2048 23:59:59 UTC
```
Use a boolean `true` value to set the endpoint as actively deprecated. 
```
Deprecation: true
```
### Sunset header
The sunset header always takes an HTTP-date timestamp and represents the date that a provider will remove the endpoint.
```
Deprecation: true
Sunset: Thu, 11 Nov 2049 23:59:59 UTC
```
