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

### tabGroups

```typescript
tabGroups: TabGroups
```

### terminals

```typescript
terminals: readonly Terminal[]
```

### visibleNotebookEditors

```typescript
visibleNotebookEditors: readonly NotebookEditor[]
```

### visibleTextEditors

```typescript
visibleTextEditors: readonly TextEditor[]
```

## Events

### onDidChangeActiveColorTheme

```typescript
onDidChangeActiveColorTheme: Event<ColorTheme>
```

### onDidChangeActiveNotebookEditor

```typescript
onDidChangeActiveNotebookEditor: Event<NotebookEditor | undefined>
```

### onDidChangeActiveTerminal

```typescript
onDidChangeActiveTerminal: Event<Terminal | undefined>
```

### onDidChangeActiveTextEditor

```typescript
onDidChangeActiveTextEditor: Event<TextEditor | undefined>
```

### onDidChangeNotebookEditorSelection

```typescript
onDidChangeNotebookEditorSelection: Event<NotebookEditorSelectionChangeEvent>
```

### onDidChangeNotebookEditorVisibleRanges

```typescript
onDidChangeNotebookEditorVisibleRanges: Event<NotebookEditorVisibleRangesChangeEvent>
```

### onDidChangeTerminalState

```typescript
onDidChangeTerminalState: Event<Terminal>
```

### onDidChangeTextEditorOptions

```typescript
onDidChangeTextEditorOptions: Event<TextEditorOptionsChangeEvent>
```

### onDidChangeTextEditorSelection

```typescript
onDidChangeTextEditorSelection: Event<TextEditorSelectionChangeEvent>
```

### onDidChangeTextEditorViewColumn

```typescript
onDidChangeTextEditorViewColumn: Event<TextEditorViewColumnChangeEvent>
```

### onDidChangeTextEditorVisibleRanges

```typescript
onDidChangeTextEditorVisibleRanges: Event<TextEditorVisibleRangesChangeEvent>
```

### onDidChangeVisibleNotebookEditors

```typescript
onDidChangeVisibleNotebookEditors: Event<readonly NotebookEditor[]>
```

### onDidChangeVisibleTextEditors

```typescript
onDidChangeVisibleTextEditors: Event<readonly TextEditor[]>
```

### onDidChangeWindowState

```typescript
onDidChangeWindowState: Event<WindowState>
```

### onDidCloseTerminal

```typescript
onDidCloseTerminal: Event<Terminal>
```

### onDidOpenTerminal

```typescript
onDidOpenTerminal: Event<Terminal>
```

## Functions

### createInputBox

```typescript
createInputBox(): InputBox
```

### createOutputChannel

```typescript
//1)
createOutputChannel(name: string, languageId?: string): OutputChannel
//2)
createOutputChannel(name: string, options: {log: true}): LogOutputChannel
```

### createQuickPick

```typescript
createQuickPick<T extends QuickPickItem>(): QuickPick<T>
```

### createStatusBarItem

```typescript
createStatusBarItem(id: string, alignment?: StatusBarAlignment, priority?: number): StatusBarItem
```

### createStatusBarItem

```typescript
createStatusBarItem(alignment?: StatusBarAlignment, priority?: number): StatusBarItem
```

### createTerminal

```typescript
createTerminal(name?: string, shellPath?: string, shellArgs?: string | readonly string[]): Terminal
```

### createTerminal

```typescript
createTerminal(options: TerminalOptions): Terminal
```

### createTerminal

```typescript
createTerminal(options: ExtensionTerminalOptions): Terminal
```

### createTextEditorDecorationType

```typescript
createTextEditorDecorationType(options: DecorationRenderOptions): TextEditorDecorationType
```

### createTreeView

```typescript
createTreeView<T>(viewId: string, options: TreeViewOptions<T>): TreeView<T>
```

### createWebviewPanel

```typescript
createWebviewPanel(viewType: string, title: string, showOptions: ViewColumn | {preserveFocus: boolean, viewColumn: ViewColumn}, options?: WebviewPanelOptions & WebviewOptions): WebviewPanel
```

### registerCustomEditorProvider

```typescript
registerCustomEditorProvider(viewType: string, provider: CustomTextEditorProvider | CustomReadonlyEditorProvider<CustomDocument> | CustomEditorProvider<CustomDocument>, options?: {supportsMultipleEditorsPerDocument: boolean, webviewOptions: WebviewPanelOptions}): Disposable
```

### registerFileDecorationProvider

```typescript
registerFileDecorationProvider(provider: FileDecorationProvider): Disposable
```

### registerTerminalLinkProvider

```typescript
registerTerminalLinkProvider(provider: TerminalLinkProvider<TerminalLink>): Disposable
```

### registerTerminalProfileProvider

```typescript
registerTerminalProfileProvider(id: string, provider: TerminalProfileProvider): Disposable
```

### registerTreeDataProvider

```typescript
registerTreeDataProvider<T>(viewId: string, treeDataProvider: TreeDataProvider<T>): Disposable
```

### registerUriHandler

```typescript
registerUriHandler(handler: UriHandler): Disposable
```

### registerWebviewPanelSerializer

```typescript
registerWebviewPanelSerializer(viewType: string, serializer: WebviewPanelSerializer<unknown>): Disposable
```

### registerWebviewViewProvider

```typescript
registerWebviewViewProvider(viewId: string, provider: WebviewViewProvider, options?: {webviewOptions: {retainContextWhenHidden: boolean}}): Disposable
```

### setStatusBarMessage

```typescript
setStatusBarMessage(text: string, hideAfterTimeout: number): Disposable
```

### setStatusBarMessage

```typescript
//1)
setStatusBarMessage(text: string, hideWhenDone: Thenable<any>): Disposable
//2)
setStatusBarMessage(text: string): Disposable
```

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

### showInputBox

```typescript
showInputBox(options?: InputBoxOptions, token?: CancellationToken): Thenable<string | undefined>
```

### showNotebookDocument

```typescript
showNotebookDocument(document: NotebookDocument, options?: NotebookDocumentShowOptions): Thenable<NotebookEditor>
```

### showOpenDialog

```typescript
showOpenDialog(options?: OpenDialogOptions): Thenable<Uri[] | undefined>
```

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

### showSaveDialog

```typescript
showSaveDialog(options?: SaveDialogOptions): Thenable<Uri | undefined>
```

### showTextDocument

```typescript
//1)
showTextDocument(document: TextDocument, column?: ViewColumn, preserveFocus?: boolean): Thenable<TextEditor>
//2)
showTextDocument(document: TextDocument, options?: TextDocumentShowOptions): Thenable<TextEditor>
//3)
showTextDocument(uri: Uri, options?: TextDocumentShowOptions): Thenable<TextEditor>
```

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

### showWorkspaceFolderPick

```typescript
showWorkspaceFolderPick(options?: WorkspaceFolderPickOptions): Thenable<WorkspaceFolder | undefined>
```

### withProgress

```typescript
withProgress<R>(options: ProgressOptions, task: (progress: Progress<{increment: number, message: string}>, token: CancellationToken) => Thenable<R>): Thenable<R>
```

### withScmProgress

```typescript
withScmProgress<R>(task: (progress: Progress<number>) => Thenable<R>): Thenable<R>
```

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
