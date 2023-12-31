# window

Namespace for dealing with the current window of the editor. That is visible and active editors, as well as, UI elements to show messages, selections, and asking for user input.

## Variables

### activeColorTheme

```typescript
activeColorTheme: ColorTheme
```

The currently active color theme as configured in the settings.
The active theme can be changed via the `workbench.colorTheme` setting.

### activeNotebookEditor

```typescript
activeNotebookEditor: NotebookEditor | undefined
```

The currently active notebook editor or `undefined`.
The active editor is the one that currently has focus or, when none has focus, the one that has changed input most recently.

### activeTerminal

```typescript
activeTerminal: Terminal | undefined
```

The currently active terminal or `undefined`.
The active terminal is the one that currently has focus or most recently had focus.

### activeTextEditor

```typescript
activeTextEditor: TextEditor | undefined
```

The currently active editor or `undefined`.
The active editor is the one that currently has focus or,
when none has focus, the one that has changed input most recently.

### state

```typescript
state: WindowState
```

Represents the current window's state.

### tabGroups

```typescript
tabGroups: TabGroups
```

Represents the grid widget within the main editor area.

### terminals

```typescript
terminals: readonly Terminal[]
```

The currently opened terminals or an empty array.

### visibleNotebookEditors

```typescript
visibleNotebookEditors: readonly NotebookEditor[]
```

The currently visible notebook editors or an empty array.

### visibleTextEditors

```typescript
visibleTextEditors: readonly TextEditor[]
```

The currently visible editors or an empty array.

## Events

### onDidChangeActiveColorTheme

```typescript
onDidChangeActiveColorTheme: Event<ColorTheme>
```

An Event which fires when the active color theme is changed or has changes.

### onDidChangeActiveNotebookEditor

```typescript
onDidChangeActiveNotebookEditor: Event<NotebookEditor | undefined>
```

An Event which fires when the active notebook editor has changed.
Note that the event also fires when the active editor changes to `undefined`.

### onDidChangeActiveTerminal

```typescript
onDidChangeActiveTerminal: Event<Terminal | undefined>
```

An Event which fires when the active terminal has changed.
Note that the event also fires when the active terminal changes to `undefined`.

### onDidChangeActiveTextEditor

```typescript
onDidChangeActiveTextEditor: Event<TextEditor | undefined>
```

An Event which fires when the active editor has changed.
Note that the event also fires when the active editor changes to `undefined`

### onDidChangeNotebookEditorSelection

```typescript
onDidChangeNotebookEditorSelection: Event<NotebookEditorSelectionChangeEvent>
```

An Event which fires when the notebook editor selections have changed.

### onDidChangeNotebookEditorVisibleRanges

```typescript
onDidChangeNotebookEditorVisibleRanges: Event<NotebookEditorVisibleRangesChangeEvent>
```

An Event which fires when the notebook editor visible ranges have changed.

### onDidChangeTerminalState

```typescript
onDidChangeTerminalState: Event<Terminal>
```

An Event which fires when a terminal's state has changed.

### onDidChangeTextEditorOptions

```typescript
onDidChangeTextEditorOptions: Event<TextEditorOptionsChangeEvent>
```

An Event which fires when the options of an editor have changed.

### onDidChangeTextEditorSelection

```typescript
onDidChangeTextEditorSelection: Event<TextEditorSelectionChangeEvent>
```

An Event which fires when the selection in an editor has changed.

### onDidChangeTextEditorViewColumn

```typescript
onDidChangeTextEditorViewColumn: Event<TextEditorViewColumnChangeEvent>
```

An Event which fires when the view column of an editor has changed.

### onDidChangeTextEditorVisibleRanges

```typescript
onDidChangeTextEditorVisibleRanges: Event<TextEditorVisibleRangesChangeEvent>
```

An Event which fires when the visible ranges of an editor has changed.

### onDidChangeVisibleNotebookEditors

```typescript
onDidChangeVisibleNotebookEditors: Event<readonly NotebookEditor[]>
```

An Event which fires when the visible notebook editors has changed.

### onDidChangeVisibleTextEditors

```typescript
onDidChangeVisibleTextEditors: Event<readonly TextEditor[]>
```

An Event which fires when the array of visible editors has changed.

### onDidChangeWindowState

```typescript
onDidChangeWindowState: Event<WindowState>
```

An Event which fires when the focus state of the current window changes.
The value of the event represent whether the window is focused.

### onDidCloseTerminal

```typescript
onDidCloseTerminal: Event<Terminal>
```

An Event which fires when a terminal is disposed.

### onDidOpenTerminal

```typescript
onDidOpenTerminal: Event<Terminal>
```

An Event which fires when a terminal has been created, editor through the createTerminal API or commands.

## Functions

### createInputBox

```typescript
createInputBox(): InputBox
```

Create a InputBox to let the user enter some text input.

Note that in many cases the more convenient showInputBox is easier to use.
createInputBox should be used when showInputBox does not offer the required flexibility.

**Returns**

+ [InputBox]
  + A new [InputBox]

### createOutputChannel

```typescript
//1)
createOutputChannel(name: string, languageId?: string): OutputChannel
//2)
createOutputChannel(name: string, options: {log: true}): LogOutputChannel
```

1)  
Create a new output channel with the given name and language id if language id is not provided, then Log is used as default language id.

You can access the visible or active output channel as a text document from visible editor or active editor and use the language id to contribute language features like syntax coloring, code lens etc...

2)  
Create a new log output channel with the given name.

**Parameter**

+ *name*: string
  + Human-readable string which will be used to represent the channel in the UI.
+ *languageId*?: string
  + The identifier of the language associated with the channel
+ *options*: {log: true}
  + options for the log output channel.

**Returns**

+ [OutputChannel]
+ [LogOutputChannel]

### createQuickPick

```typescript
createQuickPick<T extends QuickPickItem>(): QuickPick<T>
```

Creates a [QuickPick] to left the user pick an item from a list of items of type T.

Note that in many cases the more convenient showQuickPick is easier to use.
createQuickPick should be used when showQuickPick does not offer the required flexibility.

**Returns**

+ [QuickPick]&lt;T&gt;
  + A new [QuickPick]

### createStatusBarItem

```typescript
//1)
createStatusBarItem(id: string, alignment?: StatusBarAlignment, priority?: number): StatusBarItem
//2)
createStatusBarItem(alignment?: StatusBarAlignment, priority?: number): StatusBarItem
```

Create a status bar item.

**Parameter**

+ *id*: string
  + The identifier of the item.
    Must be unique within the extension.
+ *alignment*: [StatusBarAlignment]
  + The alignment of the item.
+ *priority*: number
  + The priority of the item.
    Higher values mean the item should be shown more to the left.

**Returns**

+ [StatusBarItem]
  + A new status bar item.

### createTerminal

```typescript
//1)
createTerminal(name?: string, shellPath?: string, shellArgs?: string | readonly string[]): Terminal
//2)
createTerminal(options: TerminalOptions): Terminal
//3)
createTerminal(options: ExtensionTerminalOptions): Terminal
```

Creates a Terminal with a backing shell process.
The cwd of the terminal will be the workspace directory if it exists.

+ *throws* - When running in an environment where a new process cannot be started.

**Parameter**

+ *name*?: string
  + Optional human-readable string which will be used to represent the terminal in the UI.
+ *shellPath*?: string
  + Optional path to a custom shell executable to be used in the terminal
+ *shellArgs*: string | readonly string[]
  + Optional args for the custom shell executable.
    A string can be used on Windows only which allows specifying shell args in command-line format
+ *options*: [TerminalOptions]
  + A terminalOptions object describing the characteristics of the new terminal
+ *options*: [ExtensionTerminalOptions]
  + An ExtensionTerminalOptions object describing the characteristics of the new terminal

**Returns**

+ [Terminal]
  + A new Terminal

### createTextEditorDecorationType

```typescript
createTextEditorDecorationType(options: DecorationRenderOptions): TextEditorDecorationType
```

Create a TextEditorDecorationType that can be used to add decorations to text editors.

**Parameter**

+ *options*: [DecorationRenderOptions]
  + Rendering options for the decoration type

**Returns**

+ [TextEditorDecorationType]
  + A new decoration type instance.

### createTreeView

```typescript
createTreeView<T>(viewId: string, options: TreeViewOptions<T>): TreeView<T>
```

Create a TreeView for the view contributed using the extension point `views`.

**Parameter**

+ *viewId*: string
  + Id of the view contributed using the extension point `views`.
+ *options*: [TreeViewOptions]&lt;T&gt;
  + a [TreeView]

**Returns**

+ [TreeView]&lt;T&gt;
  + a [TreeView]

### createWebviewPanel

```typescript
createWebviewPanel(
    viewType: string,
    title: string,
    showOptions: ViewColumn | {preserveFocus: boolean, viewColumn: ViewColumn},
    options?: WebviewPanelOptions & WebviewOptions):
        WebviewPanel
```

Create and show a new webview panel.

**Parameter**

+ *viewType*: string
  + Identifies the type of the webview panel.
+ *title*: string
  + Title of the panel.
+ *options*:? [WebviewPanelOptions] & [WebviewOptions]
  + Setting for the new panel.

**Returns**

+ [WebviewPanel]
  + New webview panel.

### registerCustomEditorProvider

```typescript
registerCustomEditorProvider(
    viewType: string,
    provider: 
        CustomTextEditorProvider |
        CustomReadonlyEditorProvider<CustomDocument> |
        CustomEditorProvider<CustomDocument>,
    options?: {supportsMultipleEditorsPerDocument: boolean, webviewOptions: WebviewPanelOptions}):
        Disposable
```

Register a provider for custom editors for the `viewType` contribute by the `customEditors` extension point.

When a custom editor is opened, an `onCustomEditor: viewType` activation event is fired.
Your extension must register a [CustomTextEditorProvider], [CustomReadonlyEditorProvider],
[CustomEditorProvider] for `viewType` as part of activation.

**Parameter**

+ *viewType*: string
  + Unique identifier for the custom editor provider.
    This should match the `viewType` form the `customEditors` contribution point.
+ *provider*: [CustomTextEditorProvider] |
  [CustomReadonlyEditorProvider]&lt;[CustomDocument]&gt; |
  [CustomEditorProvider]&lt;[CustomDocument]&gt;
  + Provider that resolves custom editors.
+ *options*?: {*supportsMultipleEditorsPerDocument*: boolean, *webviewOptions*: [WebviewPanelOptions]}
  + Options for the provider.

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.


### registerFileDecorationProvider

```typescript
registerFileDecorationProvider(provider: FileDecorationProvider): Disposable
```

Register a file decoration provider.

**Parameter**

+ *provider*: [FileDecorationProvider]
  + A [FileDecorationProvider].

**Returns**

+ [Disposable]
  + A [Disposable] that unregisters the provider.

### registerTerminalLinkProvider

Register provider that enables the detection and handling of links within the terminal.

```typescript
registerTerminalLinkProvider(provider: TerminalLinkProvider<TerminalLink>): Disposable
```

**Parameter**

+ *provider*: [TerminalLinkProvider]&lt;[TerminalLink]&gt;
  + The provider that provides the terminal links.

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.

### registerTerminalProfileProvider

```typescript
registerTerminalProfileProvider(id: string, provider: TerminalProfileProvider): Disposable
```

Registers a provider for a contributed terminal profile.

**Parameter**

+ *id*: string
  + The ID of the contributed terminal profile.
+ *provider*: [TerminalProfileProvider]
  + The terminal profile provider.

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.

### registerTreeDataProvider

```typescript
registerTreeDataProvider<T>(viewId: string, treeDataProvider: TreeDataProvider<T>): Disposable
```

Register a [TreeDataProvider] for the view contributed using the extension point `views`.
This will allow you to contribute data to the [TreeView] and update if the data changes.

Note To get access to the [TreeView] and perform operations on it, use [createTreeView](#createtreeview).

**Parameter**

+ *viewId*: string
  + Id of the view contributed using the extension point `views`.
+ treeDataProvider: [TreeDataProvider]&lt;T&gt;
  + A [TreeDataProvider] that provides tree data for the view.

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.

### registerUriHandler

```typescript
registerUriHandler(handler: UriHandler): Disposable
```

Registers a uri handler capable of handling system-wide uris.
In case there are multiple windows open, the topmost window will handle the uri.
A uri handler is scoped to the extension it is contributed from;
it will only be able to handle uris which re directed to the extension itself.
A uri must respect the following rules:

+ The uri-scheme must be `vscode.env.uriScheme`;
+ The uri-authority must be the extension id (e.g. `my.extension`);
+ The uri-path, -query and -fragment parts are arbitrary.

For example, if the `my.extension` extension registers a uri handler,
it will only be allowed to handle uris with the prefix `product-name://my.extension`.

An extension can only register a single uri handler in its entire activation lifetime.

Note There is an activation event `onUri` that fires when a uri directed for the current extension is about to be handled.

**Parameter**

+ *handler*: [UriHandler]
  + The uri handler to register for this extension.

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.

### registerWebviewPanelSerializer

```typescript
registerWebviewPanelSerializer(viewType: string, serializer: WebviewPanelSerializer<unknown>): Disposable
```

Registers a webview panel serializer.

Extension that support reviving should have an `"onWebviewPanel: viewType"`
activation event and make sure that `registerWebviewPanelSerializer` is called during activation.

Only a single serializer may be registered at a time for a given `viewType`.

**Parameter**

+ *viewType*: string
  + Type of the webview panel that can be serialized.
+ *serializer*: [WebviewPanelSerializer]&lt;unknown&gt;
  + Webview serializer.

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.

### registerWebviewViewProvider

```typescript
registerWebviewViewProvider(viewId: string, provider: WebviewViewProvider, options?: {webviewOptions: {retainContextWhenHidden: boolean}}): Disposable
```

Register a new provider for webview views.

**Parameter**

+ *viewId*: string
  + Unique id of the view.
    This should match the `id` from the `views` contribution in the package.json.
+ *provider*: [WebviewViewProvider]
  + Provider for the webview views.
+ *options*?: {*webviewOptions*: {*retainContextWhenHidden*: boolean}}

**Returns**

+ [Disposable]
  + Disposable that unregisters the provider.

### setStatusBarMessage

```typescript
//1)
setStatusBarMessage(text: string, hideAfterTimeout: number): Disposable
//2)
setStatusBarMessage(text: string, hideWhenDone: Thenable<any>): Disposable
//3)
setStatusBarMessage(text: string): Disposable
```

Set a message to the status bar.
This is a short hand for the more powerful status bar items.

Note that status bar messages stack and that they must be disposed when no longer used.

**Parameter**

+ *text*: string
  + The message to show, supports icon substitution as in status bar items.
+ *hideAfterTimeout*: number
  + Timeout in milliseconds after which the message will be disposed.
+ *hideWhenDone*: Thenable&lt;any&gt;
  + Thenable on which completion (resolve or reject) the message will be disposed.

**Returns**

+ [Disposable]
  + A disposable which hides the status bar message.

### showErrorMessage

```typescript
//1)
showErrorMessage<T extends string>(message: string, ...items: T[]): Thenable<T | undefined>
//2)
showErrorMessage<T extends string>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
//3)
showErrorMessage<T extends MessageItem>(message: string, ...items: T[]): Thenable<T | undefined>
//4)
showErrorMessage<T extends MessageItem>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

Show an error message.

See also [showInformationMessage](#showinformationmessage)

**Parameter**

+ *message*: string
  + The message to show.
+ *options*: [MessageOptions]
  + Configures the behaviour of the message.
+ ...*items*: T[]
  + A set of items that will be rendered as actions in the message.

**Returns**

+ Thenable&lt;T | undefined&gt;
  + A thenable that resolves to the selected item or `undefined` when being dismissed.

### showInformationMessage

```typescript
//1)
showInformationMessage<T extends string>(message: string, ...items: T[]): Thenable<T | undefined>
//2)
showInformationMessage<T extends string>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
//3)
showInformationMessage<T extends MessageItem>(message: string, ...items: T[]): Thenable<T | undefined>
//4)
showInformationMessage<T extends MessageItem>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

Show an information message to users.
Optionally provide an array pf items which will be presented as clickable buttons.

**Parameter**

+ *message*: string
  + The message to show
+ *options*: [MessageOptions]
  + Configures the behaviour of the message.
+ ...*items*: T[]
  + A set of items that will be rendered as actions in the message.

**Returns**

+ Thenable&lt;T | undefined&gt;
  + A thenable that resolves to the selected item or `undefined` when being dismissed.

### showInputBox

```typescript
showInputBox(options?: InputBoxOptions, token?: CancellationToken): Thenable<string | undefined>
```

Opens an input box to ask the user for input.

The returned value will be `undefined` if the input box was canceled (e.g. pressing ESC).
Otherwise the returned value will be the string typed by the user or
an empty string if the use did not type anything but dismissed the input box with OK.

**Parameter**

+ *options*?: [InputBoxOptions]
  + Configures the behavior of the input box.
+ *token*?: [CancellationToken]
  + A token that can be used to signal cancellation.

### showNotebookDocument

```typescript
showNotebookDocument(document: NotebookDocument, options?: NotebookDocumentShowOptions): Thenable<NotebookEditor>
```

Show the given [NotebookDocument] in a notebook editor.

**Parameter**

+ *document*: [NotebookDocument]
  + A text document to be shown.
+ *options*?: [NotebookDocumentShowOptions]
  + Editor options to configure the behavior of showing the notebook editor.

**Returns**

+ Thenable&lt;[NotebookEditor]&gt;
  + A promise that resolves to an notebook editor.

### showOpenDialog

```typescript
showOpenDialog(options?: OpenDialogOptions): Thenable<Uri[] | undefined>
```

Show a file open dialog to user which allows to select a file for opening purposes.

**Parameter**

+ *options*?: [OpenDialogOptions]
  + Options that control the dialog.

**Returns**

+ Thenable<[Uri]\[\] | undefined>
  + A promise that resolves to the selected resources or `undefined`.

### showQuickPick

```typescript
//1)
showQuickPick(items: readonly string[] | Thenable<readonly string[]>, options: QuickPickOptions & {canPickMany: true}, token?: CancellationToken): Thenable<string[] | undefined>
//2)
showQuickPick(items: readonly string[] | Thenable<readonly string[]>, options?: QuickPickOptions, token?: CancellationToken): Thenable<string | undefined>
//3)
showQuickPick<T extends QuickPickItem>(items: readonly T[] | Thenable<readonly T[]>, options: QuickPickOptions & {canPickMany: true}, token?: CancellationToken): Thenable<T[] | undefined>
//4)
showQuickPick<T extends QuickPickItem>(items: readonly T[] | Thenable<readonly T[]>, options?: QuickPickOptions, token?: CancellationToken): Thenable<T | undefined>
```

Shows a selection list allowing multiple selections.

**Parameter**

+ *items*: readonly string[] | Thenable&lt;readonly string[]&gt;
  + An array of strings, or a promise that resolves to an array of strings.
+ *options*: [QuickPickOptions] & {*canPickMany*: true}
  + Configures the behavior of the selection list.
+ *token*?: [CancellationToken]
  + A token that can be used to signal cancellation.

**Returns**

+ Thenable&lt;string[] | undefined&gt;
+ Thenable&lt;string | undefined&gt;
+ Thenable&lt;T[] | undefined&gt;
+ Thenable&lt;T | undefined&gt;
  + A promise that resolves to the selected items or `undefined`.

### showSaveDialog

```typescript
showSaveDialog(options?: SaveDialogOptions): Thenable<Uri | undefined>
```

Shows a file save dialog to the user which allows to select a file for saving-purposes.

**Parameter**

+ *options*?: [SaveDialogOptions]
  + Options that control the dialog.

**Returns**

+ Thenable&lt;[Uri] | undefined&gt;
  + A promise that resolves to the selected resource or `undefined`.

### showTextDocument

```typescript
//1)
showTextDocument(document: TextDocument, column?: ViewColumn, preserveFocus?: boolean): Thenable<TextEditor>
//2)
showTextDocument(document: TextDocument, options?: TextDocumentShowOptions): Thenable<TextEditor>
//3)
showTextDocument(uri: Uri, options?: TextDocumentShowOptions): Thenable<TextEditor>
```

Show the given document in a text editor.
A column can be provided to control where the editor is being shown.
Might change the active editor.

3) A short-hand for `openTextDocument(uri).then(document => showTextDocument(document, options))`.

**Parameter**

+ *document*: [TextDocument]
  + A text document to be shown.
+ *column*?: [ViewColumn]
  + A view column in which the editor should be shown.
    The default is the active.
    Columns that do not exist will be created as needed up to the maximum of Nine.
    Use Beside to open the editor to the side of the currently active one.
+ *preserveFocus*?: boolean
  + When `true` the editor will not take focus.
+ *uri*: [Uri]
  + A resource identifier.
+ *options*?: [TextDocumentShowOptions]
  + Editor options to configure the behavior of showing the editor.

**Returns**

+ Thenable&lt;[TextEditor]&gt;
  + A promise that resolves to an editor.


### showWarningMessage

```typescript
//1)
showWarningMessage<T extends string>(message: string, ...items: T[]): Thenable<T | undefined>
//2)
showWarningMessage<T extends string>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
//3)
showWarningMessage<T extends MessageItem>(message: string, ...items: T[]): Thenable<T | undefined>
//4)
showWarningMessage<T extends MessageItem>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

Show a warning message.

See also [showInformationMessage](#showinformationmessage)

**Parameter**

+ *message*: string
  + The message to show.
+ *options*: [MessageOptions]
  + Configures the behaviour of the message.
+ ...*items*: T[]
  + A set of items that will be rendered as actions in the message.

**Returns**

+ Thenable&lt;T | undefined&gt;
  + A thenable that resolves to the selected item or `undefined` when being dismissed.

### showWorkspaceFolderPick

```typescript
showWorkspaceFolderPick(options?: WorkspaceFolderPickOptions): Thenable<WorkspaceFolder | undefined>
```

Shows a selection list of workspace folders to pick from.
Returns `undefined` if no folder is open.

**Parameter**

+ options?: [WorkspaceFolderPickOptions]
  + Configures the behavior of the workspace folder list.

**Returns**

+ Thenable&lt;[WorkspaceFolder] | undefined&gt;
  + A promise that resolves to the workspace folder or `undefined`.

### withProgress

```typescript
withProgress<R>(options: ProgressOptions, task: (progress: Progress<{increment: number, message: string}>, token: CancellationToken) => Thenable<R>): Thenable<R>
```

Show progress in the editor.
Progress is shown while running the given callback and while the promise it returned isn't resolved nor rejected.
The location at which progress should show (and other details) is defined via the passed [ProgressOptions].

**Parameter**

+ *options*: [ProgressOptions]
+ *task*: (*progress*: [Progress]&lt;{*increment*: number, *message*: string}&gt;,
  token: [CancellationToken]) => Thenable&lt;R&gt;
  + A callback returning a promise.
    Progress state can be reported with the provided [Progress] object.
  + To report discrete progress, use `increment` to indicate how much work has been completed.
    Each call with a `increment` value will be summed up and reflected as overall progress until 100% is reached
    (a value of e.g. `10` accounts for `10%` of work done).
    `ProgressLocation.Notification` is capable of showing discrete progress.
  + To monitor if the operation has been cancelled by the user, 
    use the provided [CancellationToken].
    Note that currently only `ProgressLocation.Notification` is supporting to show a cancel button to cancel
    the long running operation.

**Returns**

+ Thenable&lt;R&gt;
  + The thenable the task-callback returned.

### withScmProgress

```typescript
withScmProgress<R>(task: (progress: Progress<number>) => Thenable<R>): Thenable<R>
```

Show progress in the Source Control viewlet while running
the given callback and while its returned promise isn't resolve or rejected.

+ *deprecated* - Use `withProgress` instead.

**Parameter**

+ *task*: (*progress*: [Progress]&lt;number&gt;) => Thenable&lt;R&gt;
  + A callback returning a promise.
  Progress increments can be reported with the provided [Progress]-object.

**Returns**

+ Thenable&lt;R&gt;
  + The thenable the task

[Terminal]: Terminal.md
[SaveDialogOptions]: SaveDialogOptions.md
[TextEditorOptionsChangeEvent]: TextEditorOptionsChangeEvent.md
[DecorationRenderOptions]: DecorationRenderOptions.md
[StatusBarItem]: StatusBarItem.md
[NotebookEditor]: NotebookEditor.md
[TextEditorViewColumnChangeEvent]: TextEditorViewColumnChangeEvent.md
[ExtensionTerminalOptions]: ExtensionTerminalOptions.md
[TabGroups]: TabGroups.md
[MessageItem]: MessageItem.md
[TerminalOptions]: TerminalOptions.md
[FileDecorationProvider]: FileDecorationProvider.md
[NotebookDocumentShowOptions]: NotebookDocumentShowOptions.md
[WebviewPanelSerializer]: WebviewPanelSerializerT.md
[WebviewOptions]: WebviewOptions.md
[TextDocumentShowOptions]: TextDocumentShowOptions.md
[Event]: EventT.md
[NotebookDocument]: NotebookDocument.md
[WebviewViewProvider]: WebviewViewProvider.md
[TerminalLinkProvider]: TerminalLinkProviderT.md
[CustomDocument]: CustomDocument.md
[TreeDataProvider]: TreeDataProviderT.md
[WindowState]: WindowState.md
[TextEditorDecorationType]: TextEditorDecorationType.md
[ViewColumn]: ViewColumn.md
[Disposable]: Disposable.md
[OutputChannel]: OutputChannel.md
[ColorTheme]: ColorTheme.md
[TextDocument]: TextDocument.md
[InputBox]: InputBox.md
[TextEditor]: TextEditor.md
[WorkspaceFolder]: WorkspaceFolder.md
[TerminalProfileProvider]: TerminalProfileProvider.md
[UriHandler]: UriHandler.md
[QuickPickOptions]: QuickPickOptions.md
[Progress]: ProgressT.md
[TreeView]: TreeViewT.md
[MessageOptions]: MessageOptions.md
[NotebookEditorVisibleRangesChangeEvent]: NotebookEditorVisibleRangesChangeEvent.md
[TextEditorVisibleRangesChangeEvent]: TextEditorVisibleRangesChangeEvent.md
[TextEditorSelectionChangeEvent]: TextEditorSelectionChangeEvent.md
[QuickPick]: QuickPickT.md
[CustomTextEditorProvider]: CustomTextEditorProvider.md
[CustomEditorProvider]: CustomEditorProviderT.md
[LogOutputChannel]: LogOutputChannel.md
[OpenDialogOptions]: OpenDialogOptions.md
[WorkspaceFolderPickOptions]: WorkspaceFolderPickOptions.md
[CustomReadonlyEditorProvider]: CustomReadonlyEditorProviderT.md
[WebviewPanelOptions]: WebviewPanelOptions.md
[NotebookEditorSelectionChangeEvent]: NotebookEditorSelectionChangeEvent.md
[TerminalLink]: TerminalLink.md
[TreeViewOptions]: TreeViewOptionsT.md
[CancellationToken]: CancellationToken.md
[ProgressOptions]: ProgressOptions.md
[StatusBarAlignment]: StatusBarAlignment.md
[Uri]: Uri.md
[QuickPickItem]: QuickPickItem.md
[WebviewPanel]: WebviewPanel.md
[InputBoxOptions]: InputBoxOptions.md
