# CallHierarchyProvider

The call hierarchy provider interface describes the contract between extensions and the call hierarchy feature which allows to browse calls and caller of function, methods, constructor etc.

## Methods

### prepareCallHierarchy

```typescript
prepareCallHierarchy(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<CallHierarchyItem | CallHierarchyItem[]>
```

### provideCallHierarchyIncomingCalls

```typescript
provideCallHierarchyIncomingCalls(item: CallHierarchyItem, token: CancellationToken): ProviderResult<CallHierarchyIncomingCall[]>
```

### provideCallHierarchyOutgoingCalls

```typescript
provideCallHierarchyOutgoingCalls(item: CallHierarchyItem, token: CancellationToken): ProviderResult<CallHierarchyOutgoingCall[]>
```

[CallHierarchyItem]: CallHierarchyItem.md
[ProviderResult]: ProviderResultT.md
[CallHierarchyOutgoingCall]: CallHierarchyOutgoingCall.md
[CallHierarchyIncomingCall]: CallHierarchyIncomingCall.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
