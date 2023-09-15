# WebviewViewProvider

Provider for creating WebviewView elements.

## Methods

### resolveWebviewView

```typescript
resolveWebviewView(webviewView: WebviewView, context: WebviewViewResolveContext<unknown>, token: CancellationToken): void | Thenable<void>
```

Revolves a webview view.

`resolveWebviewView` is called when a view first becomes visible.
This may happen when the view is first loaded or when the user hides and then shows a view again.

**Parameter**

+ *webviewView*: [WebviewView]
  + Webview view to restore.
    The provider should take ownership of this view.
    The provider must set the webview's `.html` and hook up all webview events it is interested in.
+ *context*: [WebviewViewResolveContext]
  + Additional metadata about the view being resolved.
+ *token*: [CancellationToken]
  + Cancellation token indicating that the view being provided is no longer needed.

**Returns**

+ void | Thenable&lt;void&gt;
  + Optional thenable indicating that the view has been fully resolved.

[WebviewViewResolveContext]: WebviewViewResolveContextT.md
[WebviewView]: WebviewView.md
[CancellationToken]: CancellationToken.md
