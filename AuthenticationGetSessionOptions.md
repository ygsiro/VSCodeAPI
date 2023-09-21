# AuthenticationGetSessionOptions

Options to be used when getting an AuthenticationSession from an AuthenticationProvider.

## Properties

### clearSessionPreference

```typescript
clearSessionPreference?: boolean
```

Whether the existing session preference should be cleared.

For authentication providers that support being signed into multiple accounts at once,
the user will be prompted to select an account to use when getSession is called.
This preference is remembered until getSession is called with this flag.

Note: The preference is extension specific.
So if one extension calls getSession, it will not affect the session preference for another extension calling getSession.
Additionally, the preference is set for the current workspace and also globally.
This means that new workspaces will use the "global" value at first and then when this flag is provided,
a new value can be set for that workspace.
This also means that pre-existing workspaces will not lose their preference if a new workspace sets this flag.

Default to false.

### createIfNone

```typescript
createIfNone?: boolean
```

### forceNewSession

```typescript
forceNewSession?: boolean | AuthenticationForceNewSessionOptions
```

### silent

```typescript
silent?: boolean
```

[AuthenticationForceNewSessionOptions]: AuthenticationForceNewSessionOptions.md
