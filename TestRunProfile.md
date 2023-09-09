# TestRunProfile

A TestRunProfile describes one way to execute tests in a TestController.

## Properties

### configureHandler

```typescript
configureHandler: () => void
```

### isDefault

```typescript
isDefault: boolean
```

### kind

```typescript
kind: TestRunProfileKind
```

### label

```typescript
label: string
```

### runHandler

```typescript
runHandler: (request: TestRunRequest, token: CancellationToken) => void | Thenable<void>
```

### supportsContinuousRun

```typescript
supportsContinuousRun: boolean
```

### tag

```typescript
tag: TestTag
```

## Methods

### dispose

```typescript
dispose(): void
```

