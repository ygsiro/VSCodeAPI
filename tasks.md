# tasks

Namespace for tasks functionality.

## Variables

### taskExecutions

```typescript
taskExecutions: readonly TaskExecution[]
```

## Events

### onDidEndTask

```typescript
onDidEndTask: Event<TaskEndEvent>
```

### onDidEndTaskProcess

```typescript
onDidEndTaskProcess: Event<TaskProcessEndEvent>
```

### onDidStartTask

```typescript
onDidStartTask: Event<TaskStartEvent>
```

### onDidStartTaskProcess

```typescript
onDidStartTaskProcess: Event<TaskProcessStartEvent>
```

## Functions

### executeTask

```typescript
executeTask(task: Task): Thenable<TaskExecution>
```

### fetchTasks

```typescript
fetchTasks(filter?: TaskFilter): Thenable<Task[]>
```

### registerTaskProvider

```typescript
registerTaskProvider(type: string, provider: TaskProvider<Task>): Disposable
```

