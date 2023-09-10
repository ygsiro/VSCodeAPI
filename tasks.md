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

[Task]: Task.md
[TaskProvider]: TaskProviderT.md
[TaskProcessEndEvent]: TaskProcessEndEvent.md
[TaskProcessStartEvent]: TaskProcessStartEvent.md
[Disposable]: Disposable.md
[TaskExecution]: TaskExecution.md
[TaskFilter]: TaskFilter.md
[TaskEndEvent]: TaskEndEvent.md
[Event]: EventT.md
[TaskStartEvent]: TaskStartEvent.md
