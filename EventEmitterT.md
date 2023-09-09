## EventEmitter&lt;T&gt;

An event emitter can be used to create and manage an Event for others to subscribe to. One emitter always owns one event.

Use this class if you want to provide event from within your extension, for instance inside a TextDocumentContentProvider or when providing API to other extensions.

## Constructors

```typescript
new EventEmitter<T>(): EventEmitter<T>
```

## Properties

### event

```typescript
event: Event<T>
```

## Methods

### dispose

```typescript
dispose(): void
```

### fire

```typescript
fire(data: T): void
```

