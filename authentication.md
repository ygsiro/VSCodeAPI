# authentication

Namespace for authentication.

## Events

### onDidChangeSessions

```typescript
onDidChangeSessions: Event<AuthenticationSessionsChangeEvent>
```

An Event which fires when the authentication sessions of an authentication provider have been added, removed, or changed.

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

Get an authentication session matching the desired scopes.
Rejects if a provider with providerId is not registered,
or if the user does not consent to sharing authentication information with the extension.
If there are multiple sessions with the same scopes, the user will be shown a quickpick to select which account they would like to use.

Currently, there are only two authentication providers that are contributed from built in extensions to
the editor that implement GitHub and Microsoft authentication: their providerId's are `github` and `microsoft`.

**Parameter**

+ *providerId*: string
  + The id of the provider to use
+ *scopes*: readonly string[]
  + A list of scopes representing the permissions requested.
    These are dependent on the authentication provider.
+ *options*: [AuthenticationGetSessionOptions] & {*createIfNone*: true}
+ *options*: [AuthenticationForceNewSessionOptions] & {*forceNewSession*: true | [AuthenticationForceNewSessionOptions]}
+ *options*?: [AuthenticationGetSessionOptions]
  + The [AuthenticationGetSessionOptions] to use

**Returns**

+ Thenable&lt;[AuthenticationSession]&gt;
  + A thenable that resolves to an authentication session.
  + 3)if available, or undefined if there are no sessions.

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
