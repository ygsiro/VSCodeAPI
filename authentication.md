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
getSession(providerId: string, scopes: readonly string[], options: AuthenticationGetSessionOptions & {createIfNone: true}): Thenable<AuthenticationSession>
```

### getSession

```typescript
getSession(providerId: string, scopes: readonly string[], options: AuthenticationGetSessionOptions & {forceNewSession: true | AuthenticationForceNewSessionOptions}): Thenable<AuthenticationSession>
```

### getSession

```typescript
getSession(providerId: string, scopes: readonly string[], options?: AuthenticationGetSessionOptions): Thenable<AuthenticationSession | undefined>
```

### registerAuthenticationProvider

```typescript
registerAuthenticationProvider(id: string, label: string, provider: AuthenticationProvider, options?: AuthenticationProviderOptions): Disposable
```

