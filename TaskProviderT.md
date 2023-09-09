# TaskProvider<T>

A task provider allows to add tasks to the task service. A task provider is registered via registerTaskProvider.

## Methods

### provideTasks

```typescript
provideTasks(token: CancellationToken): ProviderResult<T[]>
```

### resolveTask

```typescript
resolveTask(task: T, token: CancellationToken): ProviderResult<T>
```

