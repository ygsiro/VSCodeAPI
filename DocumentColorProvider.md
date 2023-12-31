# DocumentColorProvider

The document color provider defines the contract between extensions and feature of picking and modifying colors in the editor.

## Methods

### provideColorPresentations

```typescript
provideColorPresentations(color: Color, context: {document: TextDocument, range: Range}, token: CancellationToken): ProviderResult<ColorPresentation[]>
```

### provideDocumentColors

```typescript
provideDocumentColors(document: TextDocument, token: CancellationToken): ProviderResult<ColorInformation[]>
```

[Color]: Color.md
[Range]: Range.md
[ProviderResult]: ProviderResultT.md
[ColorInformation]: ColorInformation.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
[ColorPresentation]: ColorPresentation.md
