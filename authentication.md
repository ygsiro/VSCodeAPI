# authentication

Namespace for authentication.

## Events

### onDidChangeSessions

```typescript
onDidChangeSessions: Event<AuthenticationSessionsChangeEvent>
```

## Functions

### getSession

```typescript
//1)
getSession(providerId: string, scopes: readonly string[], options: AuthenticationGetSessionOptions & {createIfNone: true}): Thenable<AuthenticationSession>
//2)
getSession(providerId: string, scopes: readonly string[], options: AuthenticationGetSessionOptions & {forceNewSession: true | AuthenticationForceNewSessionOptions}): Thenable<AuthenticationSession>
//3)
getSession(providerId: string, scopes: readonly string[], options?: AuthenticationGetSessionOptions): Thenable<AuthenticationSession | undefined>
```

### registerAuthenticationProvider

```typescript
registerAuthenticationProvider(id: string, label: string, provider: AuthenticationProvider, options?: AuthenticationProviderOptions): Disposable
```

[AuthenticationSessionsChangeEvent]: AuthenticationSessionsChangeEvent.md
[AuthenticationProviderOptions]: AuthenticationProviderOptions.md
[AuthenticationForceNewSessionOptions]: AuthenticationForceNewSessionOptions.md
[AuthenticationProvider]: AuthenticationProvider.md
[Disposable]: Disposable.md
[AuthenticationGetSessionOptions]: AuthenticationGetSessionOptions.md
[AuthenticationSession]: AuthenticationSession.md
[Event]: EventT.md
