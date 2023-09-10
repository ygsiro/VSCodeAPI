# TestRun

A TestRun represents an in-progress or completed test run and provides methods to report the state of individual tests in the run.

## Properties

### isPersisted

```typescript
isPersisted: boolean
```

### name

```typescript
name: string
```

### token

```typescript
token: CancellationToken
```

## Methods

### appendOutput

```typescript
appendOutput(output: string, location?: Location, test?: TestItem): void
```

### end

```typescript
end(): void
```

### enqueued

```typescript
enqueued(test: TestItem): void
```

### errored

```typescript
errored(test: TestItem, message: TestMessage | readonly TestMessage[], duration?: number): void
```

### failed

```typescript
failed(test: TestItem, message: TestMessage | readonly TestMessage[], duration?: number): void
```

### passed

```typescript
passed(test: TestItem, duration?: number): void
```

### skipped

```typescript
skipped(test: TestItem): void
```

### started

```typescript
started(test: TestItem): void
```

[TestItem]: TestItem.md
[TestMessage]: TestMessage.md
[CancellationToken]: CancellationToken.md
[Locaation]: Location.md
