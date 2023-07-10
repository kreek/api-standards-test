# Performance & Availability

Government digital services have gained a reputation for lacking performance and
reliability in the past. This reputation was not unwarranted and was largely due
to the inherent complexity of connecting multiple (legacy) services and allowing
their imperfections to bubble up to consumers. Your API's goal should be to
abstract away that complexity, catch any upstream errors, and optimize
performance.

With the correct strategies in place, your API can be as performant and reliable
as a greenfield project. And if you're working on a new API without any
dependencies, make performance and reliability a priority, as an API by nature,
is a dependency for consuming applications.

## Performance

!!! warning "Requirement"
    - APIs **must** respond to requests in less than 10 seconds or the gateway will return a 504 error.

!!! success "Guidance"
    - APIs **should** aim to respond to requests in less than 1 second.
    - If an API can't respond to requests in under 10 seconds, it **should** implement
      an asynchronous pattern that returns a response immediately and processes the request
      in the background.

APIs must respond to requests within a ten-second timeframe. If a response takes
longer than this, the gateway will interpret this delay as a timeout and return
a 504 error, indicating a server-side timeout. While the ten-second response is
a hard limit, APIs should aim to respond to requests in under one second and
ideally a few milliseconds.

## Availability

!!! success "Guidance"
    - APIs **should** be available 99.9% of the time in the production environment.
    - APIs **should** be available 99.0% of the time in the sandbox environment.

APIs should strive to have 99.9% availability in production and 99.0% in the sandbox environment.
The Lighthouse team is willing to help work through technical or policy barriers to achieve this.

### Managing downtime in dependencies

!!! warning "Requirement"
    - APIs **must not** pass upstream errors onto consumers.

Most APIs within the VA depend on one or more services with various levels of reliability, and due
to contract constraints, API teams often can't dictate the pace of change in their upstream dependencies.
However, APIs must never pass a consumer upstream unexpected (500) or service unavailability (503, 504) errors.

Instead, an API should gracefully handle unexpected upstream errors, downtime, and timeouts with clear,
consistent, and forthright information so that consuming applications know the issue is from a dependency
and can reliably surface an appropriate message in their client applications.

For suggestions on mapping upstream errors, see [Choosing an error code](../errors/index.md#choosing-an-error-code).
