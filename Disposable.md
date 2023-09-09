# Disposable

Represents a type which can release resources, such as event listening or a timer.

## Static

### from

```typescript
from(...disposableLikes: {dispose: () => any}[]): Disposable
```

## Constructors

```typescript
new Disposable(callOnDispose: () => any): Disposable
```

## Methods

### dispose

```typescript
dispose(): any
```

