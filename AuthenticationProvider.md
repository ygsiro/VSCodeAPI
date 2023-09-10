# AuthenticationProvider

A provider for performing authentication to a service.

## Events

### onDidChangeSessions

```typescript
onDidChangeSessions: Event<AuthenticationProviderAuthenticationSessionsChangeEvent>
```

## Methods

### createSession

```typescript
createSession(scopes: readonly string[]): Thenable<AuthenticationSession>
```

### getSessions

```typescript
getSessions(scopes?: readonly string[]): Thenable<readonly AuthenticationSession[]>
```

### removeSession

```typescript
removeSession(sessionId: string): Thenable<void>
```

[Event]: EventT.md
[AuthenticationSession]: AuthenticationSession.md
[AuthenticationProviderAuthenticationSessionsChangeEvent]: AuthenticationProviderAuthenticationSessionsChangeEvent.md
