# CallHierarchyOutgoingCall

Represents an outgoing call, e.g. calling a getter from a method or a method from a constructor etc.

## Constructors

```typescript
new CallHierarchyOutgoingCall(item: CallHierarchyItem, fromRanges: Range[]): CallHierarchyOutgoingCall
```

## Properties

### fromRanges

```typescript
fromRanges: Range[]
```

### to

```typescript
to: CallHierarchyItem
```

