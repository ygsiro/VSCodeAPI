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

Whether login should be performed if there is no matching session.

If true, a model dialog will be shown asking the user to sign in.
If false, a numbered badge will be shown on the accounts activity bar icon.
An entry for the extension will be added under the menu to sign in.
This allows quietly prompting the user to sign in.

If there is a matching session but the extension has not been granted access to it,
setting this to true will also result in an immediate model dialog,
and false will add a numbered badge to the accounts icon.

Default to false.

Note: you cannot use this option with silent.

### forceNewSession

```typescript
forceNewSession?: boolean | AuthenticationForceNewSessionOptions
```

Whether we should attempt to reauthenticate even if there is already a session available.

If true, a model dialog will be shown asking the user to sign in again.
This is mostly used for scenarios where the token needs to be re minted because it has lost some authentication.

If there are no existing sessions and forceNewSession is true,
it will behave identically to createIfNone.

The defaults to false.

### silent

```typescript
silent?: boolean
```

Whether we should show the indication to sign in in the Accounts menu.

If false, the user will be shown a badge on the Accounts menu with an option to sign in for the extension.
If true, no indication will be shown.

Defaults to false.

Note: you cannot use this option with any other options that prompt the user like createIfNone.

[AuthenticationForceNewSessionOptions]: AuthenticationForceNewSessionOptions.md
