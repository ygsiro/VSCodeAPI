# Webview

Displays html content, similarly to an iframe.

## Events

### onDidReceiveMessage

```typescript
onDidReceiveMessage: Event<any>
```

Fined when the webview content posts a message.

webview content can post strings or json serializable objects back to an extension.
They cannot post `Blob`, `File`, `ImageData` and other DOM specific objects since the extension that receives the message does not run in a browser environment.

## Properties

### cspSource

```typescript
cspSource: string
```

Content security policy source for webview resources.
This is the origin that should be used in a content security policy rule:

```typescript
`img-src https: ${webview.cspSource} ...;`;
```

### html

```typescript
html: string
```

HTML contents of the webview.

This should be a complete, valid html document.
Changing this property causes the webview to be reloaded.

Webviews are sandboxed from normal extension process, so all communication with the webview must use message passing.
To send a message from the extension to the webview, use postMessage.
To send message from the webview back to an extension, use the `acquireVsCodeApi` function inside the webview to get a handle to the editor's api and then call `.postMessage()`:

```html
<script>
    const vscode = acquireVsCodeApi(); // acquireVsCodeApi can only be invoked once
    vscode.postMessage({ message: `hello!` });
</script>
```

To load a resources from the workspace inside a webview, use the asWebviewUri method and ensure the resource's directory is listed in localResourceRoots.

Keep in mind that even though webviews are sandboxed, they still allow running scripts and loading arbitrary content,
so extensions must follow all standard web security best practices when working with webviews.
This includes properly sanitizing all untrusted input (including content from the workspace) and setting a content security policy.

### options

```typescript
options: WebviewOptions
```

Content settings for the webview.

## Methods

### asWebviewUri

```typescript
asWebviewUri(localResource: Uri): Uri
```

Convert a uri for the local file system to one that can be used inside webviews.

Webviews cannot directly load resources from the workspace or local file system using `file:` uris.
The `asWebViewUri` function tasks a local `file:` uri and converts it into a uri that can be used inside of a webview to load the same resource:

```typescript
webview.html = `<img src="${webview.asWebViewUri(
    vscode.Uri.file('/Users/code/workspace/cat.gif')
)}">`;
```

**Parameter**

+ *localResource*: [Uri]

**Returns**

[Uri]

### postMessage

```typescript
postMessage(message: any): Thenable<boolean>
```

Post a message to the webview content.

Messages are only delivered if the webview is live (either visible or in the background with `retainContextWhenHidden`).

**Parameter**

+ *message*: any
  + Body of the message.
    This must be a string or other json serializable object.
  + For older versions of vscode, if an `ArrayBuffer` is included in `message`,
    it will not be serialized properly and will not be received by the webview.
    Similarly any TypedArrays, such as a `Uint8Array`, will be very inefficiently
    serialized and will also not be recreated as a typed array inside the webview.
  + However if your extension targets vscode 1.57+ in the `engines` field of its `package.json`,
    any `ArrayBuffer` values that appear in `message` will be more efficiently transferred to the webview and will also be correctly recreated inside of the webview.

**Returns**

+ Thenable&lt;boolean&gt;
  + A promise that resolves when the message is posted to a webview or when it is dropped because the message was not deliverable.
  + Returns `true` if  the message was posted to the webview.
    Messages can only be posted to live webviews(i.e. either visible webviews or hidden webviews that set `retainContextWhenHidden`).
  + A response of `true` does not mean that the message was actually received by the webview.
    For example, no message listeners may be have been hooked up inside the webview may have been destroyed after the message was posted but before it was received.
  + If you want confirm that a message as actually received, you can try having your webview posting a confirmation message back to your extension.

[Event]: EventT.md
[Uri]: Uri.md
[WebviewOptions]: WebviewOptions.md
