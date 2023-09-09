# CancellationToken

A cancellation token is passed to an asynchronous or long running operation to request cancellation, like cancelling a request for completion items because the user continued to type.

To get an instance of a CancellationToken use a CancellationTokenSource.

## Properties

### isCancellationRequested

```typescript
isCancellationRequested: boolean
```

### onCancellationRequested

```typescript
onCancellationRequested: Event<any>
```

