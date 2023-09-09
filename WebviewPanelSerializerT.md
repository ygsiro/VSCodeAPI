## WebviewPanelSerializer&lt;T&gt;

Restore webview panels that have been persisted when vscode shuts down.

There are two types of webview persistence:

Persistence within a session.
Persistence across sessions (across restarts of the editor).
A WebviewPanelSerializer is only required for the second case: persisting a webview across sessions.

Persistence within a session allows a webview to save its state when it becomes hidden and restore its content from this state when it becomes visible again. It is powered entirely by the webview content itself. To save off a persisted state, call acquireVsCodeApi().setState() with any json serializable object. To restore the state again, call getState()

```typescript
// Within the webview
const vscode = acquireVsCodeApi();

// Get existing state
const oldState = vscode.getState() || { value: 0 };

// Update state
setState({ value: oldState.value + 1 });
```

A WebviewPanelSerializer extends this persistence across restarts of the editor. When the editor is shutdown, it will save off the state from setState of all webviews that have a serializer. When the webview first becomes visible after the restart, this state is passed to deserializeWebviewPanel. The extension can then restore the old WebviewPanel from this state.

## Methods

### deserializeWebviewPanel

```typescript
deserializeWebviewPanel(webviewPanel: WebviewPanel, state: T): Thenable<void>
```

