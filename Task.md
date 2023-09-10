# Task

A task to execute

## Constructors

```typescript
new Task(taskDefinition: TaskDefinition, scope: WorkspaceFolder | Global | Workspace, name: string, source: string, execution?: ProcessExecution | ShellExecution | CustomExecution, problemMatchers?: string | string[]): Task
```

```typescript
new Task(taskDefinition: TaskDefinition, name: string, source: string, execution?: ProcessExecution | ShellExecution, problemMatchers?: string | string[]): Task
```

## Properties

### definition

```typescript
definition: TaskDefinition
```

### detail

```typescript
detail?: string
```

### execution

```typescript
execution?: ProcessExecution | ShellExecution | CustomExecution
```

### group

```typescript
group?: TaskGroup
```

### isBackground

```typescript
isBackground: boolean
```

### name

```typescript
name: string
```

### presentationOptions

```typescript
presentationOptions: TaskPresentationOptions
```

### problemMatchers

```typescript
problemMatchers: string[]
```

### runOptions

```typescript
runOptions: RunOptions
```

### scope

```typescript
scope: WorkspaceFolder | Global | Workspace
```

### source

```typescript
source: string
```

[ProcessExecution]: ProcessExecution.md
[RunOptions]: RunOptions.md
[TaskPresentationOptions]: TaskPresentationOptions.md
[WorkspaceFolder]: WorkspaceFolder.md
[TaskGroup]: TaskGroup.md
[ShellExecution]: ShellExecution.md
[TaskDefinition]: TaskDefinition.md
[CustomExecution]: CustomExecution.md
