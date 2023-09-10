# languages

Namespace for participating in language-specific editor features, like IntelliSense, code actions, diagnostics etc.

Many programming languages exist and there is huge variety in syntaxes, semantics, and paradigms. Despite that, features like automatic word-completion, code navigation, or code checking have become popular across different tools for different programming languages.

The editor provides an API that makes it simple to provide such common features by having all UI and actions already in place and by allowing you to participate by providing data only. For instance, to contribute a hover all you have to do is provide a function that can be called with a TextDocument and a Position returning hover info. The rest, like tracking the mouse, positioning the hover, keeping the hover stable etc. is taken care of by the editor.

```typescript
languages.registerHoverProvider('javascript', {
  provideHover(document, position, token) {
    return new Hover('I am a hover!');
  }
});
```

Registration is done using a document selector which is either a language id, like javascript or a more complex filter like { language: 'typescript', scheme: 'file' }. Matching a document against such a selector will result in a score that is used to determine if and how a provider shall be used. When scores are equal the provider that came last wins. For features that allow full arity, like hover, the score is only checked to be >0, for other features, like IntelliSense the score is used for determining the order in which providers are asked to participate.

## Events

### onDidChangeDiagnostics

```typescript
onDidChangeDiagnostics: Event<DiagnosticChangeEvent>
```

## Functions

### createDiagnosticCollection

```typescript
createDiagnosticCollection(name?: string): DiagnosticCollection
```

### createLanguageStatusItem

```typescript
createLanguageStatusItem(id: string, selector: DocumentSelector): LanguageStatusItem
```

### getDiagnostics

```typescript
getDiagnostics(resource: Uri): Diagnostic[]
```

### getDiagnostics

```typescript
getDiagnostics(): [Uri, Diagnostic[]][]
```

### getLanguages

```typescript
getLanguages(): Thenable<string[]>
```

### match

```typescript
match(selector: DocumentSelector, document: TextDocument): number
```

### registerCallHierarchyProvider

```typescript
registerCallHierarchyProvider(selector: DocumentSelector, provider: CallHierarchyProvider): Disposable
```

### registerCodeActionsProvider

```typescript
registerCodeActionsProvider(selector: DocumentSelector, provider: CodeActionProvider<CodeAction>, metadata?: CodeActionProviderMetadata): Disposable
```

### registerCodeLensProvider

```typescript
registerCodeLensProvider(selector: DocumentSelector, provider: CodeLensProvider<CodeLens>): Disposable
```

### registerColorProvider

```typescript
registerColorProvider(selector: DocumentSelector, provider: DocumentColorProvider): Disposable
```

### registerCompletionItemProvider

```typescript
registerCompletionItemProvider(selector: DocumentSelector, provider: CompletionItemProvider<CompletionItem>, ...triggerCharacters: string[]): Disposable
```

### registerDeclarationProvider

```typescript
registerDeclarationProvider(selector: DocumentSelector, provider: DeclarationProvider): Disposable
```

### registerDefinitionProvider

```typescript
registerDefinitionProvider(selector: DocumentSelector, provider: DefinitionProvider): Disposable
```

### registerDocumentDropEditProvider

```typescript
registerDocumentDropEditProvider(selector: DocumentSelector, provider: DocumentDropEditProvider): Disposable
```

### registerDocumentFormattingEditProvider

```typescript
registerDocumentFormattingEditProvider(selector: DocumentSelector, provider: DocumentFormattingEditProvider): Disposable
```

### registerDocumentHighlightProvider

```typescript
registerDocumentHighlightProvider(selector: DocumentSelector, provider: DocumentHighlightProvider): Disposable
```

### registerDocumentLinkProvider

```typescript
registerDocumentLinkProvider(selector: DocumentSelector, provider: DocumentLinkProvider<DocumentLink>): Disposable
```

### registerDocumentRangeFormattingEditProvider

```typescript
registerDocumentRangeFormattingEditProvider(selector: DocumentSelector, provider: DocumentRangeFormattingEditProvider): Disposable
```

### registerDocumentRangeSemanticTokensProvider

```typescript
registerDocumentRangeSemanticTokensProvider(selector: DocumentSelector, provider: DocumentRangeSemanticTokensProvider, legend: SemanticTokensLegend): Disposable
```

### registerDocumentSemanticTokensProvider

```typescript
registerDocumentSemanticTokensProvider(selector: DocumentSelector, provider: DocumentSemanticTokensProvider, legend: SemanticTokensLegend): Disposable
```

### registerDocumentSymbolProvider

```typescript
registerDocumentSymbolProvider(selector: DocumentSelector, provider: DocumentSymbolProvider, metaData?: DocumentSymbolProviderMetadata): Disposable
```

### registerEvaluatableExpressionProvider

```typescript
registerEvaluatableExpressionProvider(selector: DocumentSelector, provider: EvaluatableExpressionProvider): Disposable
```

### registerFoldingRangeProvider

```typescript
registerFoldingRangeProvider(selector: DocumentSelector, provider: FoldingRangeProvider): Disposable
```

### registerHoverProvider

```typescript
registerHoverProvider(selector: DocumentSelector, provider: HoverProvider): Disposable
```

### registerImplementationProvider

```typescript
registerImplementationProvider(selector: DocumentSelector, provider: ImplementationProvider): Disposable
```

### registerInlayHintsProvider

```typescript
registerInlayHintsProvider(selector: DocumentSelector, provider: InlayHintsProvider<InlayHint>): Disposable
```

### registerInlineCompletionItemProvider

```typescript
registerInlineCompletionItemProvider(selector: DocumentSelector, provider: InlineCompletionItemProvider): Disposable
```

### registerInlineValuesProvider

```typescript
registerInlineValuesProvider(selector: DocumentSelector, provider: InlineValuesProvider): Disposable
```

### registerLinkedEditingRangeProvider

```typescript
registerLinkedEditingRangeProvider(selector: DocumentSelector, provider: LinkedEditingRangeProvider): Disposable
```

### registerOnTypeFormattingEditProvider

```typescript
registerOnTypeFormattingEditProvider(selector: DocumentSelector, provider: OnTypeFormattingEditProvider, firstTriggerCharacter: string, ...moreTriggerCharacter: string[]): Disposable
```

### registerReferenceProvider

```typescript
registerReferenceProvider(selector: DocumentSelector, provider: ReferenceProvider): Disposable
```

### registerRenameProvider

```typescript
registerRenameProvider(selector: DocumentSelector, provider: RenameProvider): Disposable
```

### registerSelectionRangeProvider

```typescript
registerSelectionRangeProvider(selector: DocumentSelector, provider: SelectionRangeProvider): Disposable
```

### registerSignatureHelpProvider

```typescript
registerSignatureHelpProvider(selector: DocumentSelector, provider: SignatureHelpProvider, ...triggerCharacters: string[]): Disposable
```

### registerSignatureHelpProvider

```typescript
registerSignatureHelpProvider(selector: DocumentSelector, provider: SignatureHelpProvider, metadata: SignatureHelpProviderMetadata): Disposable
```

### registerTypeDefinitionProvider

```typescript
registerTypeDefinitionProvider(selector: DocumentSelector, provider: TypeDefinitionProvider): Disposable
```

### registerTypeHierarchyProvider

```typescript
registerTypeHierarchyProvider(selector: DocumentSelector, provider: TypeHierarchyProvider): Disposable
```

### registerWorkspaceSymbolProvider

```typescript
registerWorkspaceSymbolProvider(provider: WorkspaceSymbolProvider<SymbolInformation>): Disposable
```

### setLanguageConfiguration

```typescript
setLanguageConfiguration(language: string, configuration: LanguageConfiguration): Disposable
```

### setTextDocumentLanguage

```typescript
setTextDocumentLanguage(document: TextDocument, languageId: string): Thenable<TextDocument>
```

[DocumentRangeSemanticTokensProvider]: DocumentRangeSemanticTokensProvider.md
[SemanticTokensLegend]: SemanticTokensLegend.md
[CallHierarchyProvider]: CallHierarchyProvider.md
[DocumentColorProvider]: DocumentColorProvider.md
[TypeHierarchyProvider]: TypeHierarchyProvider.md
[ReferenceProvider]: ReferenceProvider.md
[CompletionItemProvider]: CompletionItemProviderT.md
[DeclarationProvider]: DeclarationProvider.md
[InlayHintsProvider]: InlayHintsProviderT.md
[Hover]: Hover.md
[SignatureHelpProviderMetadata]: SignatureHelpProviderMetadata.md
[Event]: EventT.md
[ImplementationProvider]: ImplementationProvider.md
[CodeActionProvider]: CodeActionProviderT.md
[InlineCompletionItemProvider]: InlineCompletionItemProvider.md
[DocumentSymbolProviderMetadata]: DocumentSymbolProviderMetadata.md
[SignatureHelpProvider]: SignatureHelpProvider.md
[LanguageStatusItem]: LanguageStatusItem.md
[TypeDefinitionProvider]: TypeDefinitionProvider.md
[Disposable]: Disposable.md
[CodeLensProvider]: CodeLensProviderT.md
[TextDocument]: TextDocument.md
[LanguageConfiguration]: LanguageConfiguration.md
[DocumentLinkProvider]: DocumentLinkProviderT.md
[Diagnostic]: Diagnostic.md
[RenameProvider]: RenameProvider.md
[DocumentSemanticTokensProvider]: DocumentSemanticTokensProvider.md
[DocumentLink]: DocumentLink.md
[OnTypeFormattingEditProvider]: OnTypeFormattingEditProvider.md
[CompletionItem]: CompletionItem.md
[HoverProvider]: HoverProvider.md
[EvaluatableExpressionProvider]: EvaluatableExpressionProvider.md
[CodeAction]: CodeAction.md
[DefinitionProvider]: DefinitionProvider.md
[SymbolInformation]: SymbolInformation.md
[FoldingRangeProvider]: FoldingRangeProvider.md
[SelectionRangeProvider]: SelectionRangeProvider.md
[InlineValuesProvider]: InlineValuesProvider.md
[DiagnosticCollection]: DiagnosticCollection.md
[DocumentRangeFormattingEditProvider]: DocumentRangeFormattingEditProvider.md
[DocumentDropEditProvider]: DocumentDropEditProvider.md
[DocumentSymbolProvider]: DocumentSymbolProvider.md
[DocumentHighlightProvider]: DocumentHighlightProvider.md
[Uri]: Uri.md
[DocumentFormattingEditProvider]: DocumentFormattingEditProvider.md
[InlayHint]: InlayHint.md
[WorkspaceSymbolProvider]: WorkspaceSymbolProviderT.md
[DocumentSelector]: DocumentSelector.md
[CodeLens]: CodeLens.md
[LinkedEditingRangeProvider]: LinkedEditingRangeProvider.md
[CodeActionProviderMetadata]: CodeActionProviderMetadata.md
[DiagnosticChangeEvent]: DiagnosticChangeEvent.md
