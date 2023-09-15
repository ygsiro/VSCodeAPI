# WebviewOptions

Content settings for a webview.

## Properties

### enableCommandUris

```typescript
enableCommandUris?: boolean | readonly string[]
```

Controls whether command uris are enabled in webview content or not.

Defaults to `false` (command uris are disabled).

If you pass in an array, only the commands in the array are allowed.

### enableForms

```typescript
enableForms?: boolean
```

Controls whether forms are enabled in the webview content or not.

Default to true if `scripts are enabled`.
Otherwise defaults to `false`.
Explicitly setting this property to either `true` or `false` overrides the default.

### enableScripts

```typescript
enableScripts?: boolean
```

Controls whether scripts are enabled in the webview content or not.

Default to `false` (scripts-disabled).

### localResourceRoots

```typescript
localResourceRoots?: readonly Uri[]
```

Root paths from which the webview can load local (filesystem) resource using uris from `asWebviewUri`

Default to the root folders of the current workspace plus the extension's install directory.

Pass in an empty array to disallow access to any local resources.

### portMapping

```typescript
portMapping?: readonly WebviewPortMapping[]
```

Mappings of localhost port used inside the webview.

Port mapping allow webviews to transparently define how localhost ports are resolved.
This can be used to allow using a static localhost port inside the webview that is resolved to random port that a service is running on.

If a webview accesses localhost content, we recommend that you specify port mappings even if the `webviewPort` and `extensionHostPort` ports are the same.

Note that port mappings only work for `http` or `https` urls.
Websocket urls (e.g. `ws://localhost:3000`) cannot be mapped to another port.

[Uri]: Uri.md
[WebviewPortMapping]: WebviewPortMapping.md
