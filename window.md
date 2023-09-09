# window

Namespace for dealing with the current window of the editor. That is visible and active editors, as well as, UI elements to show messages, selections, and asking for user input.

## Variables

### activeColorTheme

```typescript
activeColorTheme: ColorTheme
```

### activeNotebookEditor

```typescript
activeNotebookEditor: NotebookEditor | undefined
```

### activeTerminal

```typescript
activeTerminal: Terminal | undefined
```

### activeTextEditor

```typescript
activeTextEditor: TextEditor | undefined
```

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
createOutputChannel(name: string, languageId?: string): OutputChannel
```

### createOutputChannel

```typescript
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
setStatusBarMessage(text: string, hideWhenDone: Thenable<any>): Disposable
```

### setStatusBarMessage

```typescript
setStatusBarMessage(text: string): Disposable
```

### showErrorMessage

```typescript
showErrorMessage<T extends string>(message: string, ...items: T[]): Thenable<T | undefined>
```

### showErrorMessage

```typescript
showErrorMessage<T extends string>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

### showErrorMessage

```typescript
showErrorMessage<T extends MessageItem>(message: string, ...items: T[]): Thenable<T | undefined>
```

### showErrorMessage

```typescript
showErrorMessage<T extends MessageItem>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

### showInformationMessage

```typescript
showInformationMessage<T extends string>(message: string, ...items: T[]): Thenable<T | undefined>
```

### showInformationMessage

```typescript
showInformationMessage<T extends string>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

### showInformationMessage

```typescript
showInformationMessage<T extends MessageItem>(message: string, ...items: T[]): Thenable<T | undefined>
```

### showInformationMessage

```typescript
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
showQuickPick(items: readonly string[] | Thenable<readonly string[]>, options: QuickPickOptions & {canPickMany: true}, token?: CancellationToken): Thenable<string[] | undefined>
```

### showQuickPick

```typescript
showQuickPick(items: readonly string[] | Thenable<readonly string[]>, options?: QuickPickOptions, token?: CancellationToken): Thenable<string | undefined>
```

### showQuickPick

```typescript
showQuickPick<T extends QuickPickItem>(items: readonly T[] | Thenable<readonly T[]>, options: QuickPickOptions & {canPickMany: true}, token?: CancellationToken): Thenable<T[] | undefined>
```

### showQuickPick

```typescript
showQuickPick<T extends QuickPickItem>(items: readonly T[] | Thenable<readonly T[]>, options?: QuickPickOptions, token?: CancellationToken): Thenable<T | undefined>
```

### showSaveDialog

```typescript
showSaveDialog(options?: SaveDialogOptions): Thenable<Uri | undefined>
```

### showTextDocument

```typescript
showTextDocument(document: TextDocument, column?: ViewColumn, preserveFocus?: boolean): Thenable<TextEditor>
```

### showTextDocument

```typescript
showTextDocument(document: TextDocument, options?: TextDocumentShowOptions): Thenable<TextEditor>
```

### showTextDocument

```typescript
showTextDocument(uri: Uri, options?: TextDocumentShowOptions): Thenable<TextEditor>
```

### showWarningMessage

```typescript
showWarningMessage<T extends string>(message: string, ...items: T[]): Thenable<T | undefined>
```

### showWarningMessage

```typescript
showWarningMessage<T extends string>(message: string, options: MessageOptions, ...items: T[]): Thenable<T | undefined>
```

### showWarningMessage

```typescript
showWarningMessage<T extends MessageItem>(message: string, ...items: T[]): Thenable<T | undefined>
```

### showWarningMessage

```typescript
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

