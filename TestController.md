# TestController

Entry point to discover and execute tests. It contains items which are used to populate the editor UI, and is associated with run profiles to allow for tests to be executed.

## Properties

### id

```typescript
id: string
```

### items

```typescript
items: TestItemCollection
```

### label

```typescript
label: string
```

### refreshHandler

```typescript
refreshHandler: (token: CancellationToken) => void | Thenable<void>
```

### resolveHandler

```typescript
resolveHandler?: (item: TestItem) => void | Thenable<void>
```

## Methods

### createRunProfile

```typescript
createRunProfile(label: string, kind: TestRunProfileKind, runHandler: (request: TestRunRequest, token: CancellationToken) => void | Thenable<void>, isDefault?: boolean, tag?: TestTag, supportsContinuousRun?: boolean): TestRunProfile
```

### createTestItem

```typescript
createTestItem(id: string, label: string, uri?: Uri): TestItem
```

### createTestRun

```typescript
createTestRun(request: TestRunRequest, name?: string, persist?: boolean): TestRun
```

### dispose

```typescript
dispose(): void
```

### invalidateTestResults

```typescript
invalidateTestResults(items?: TestItem | readonly TestItem[]): void
```

[TestItem]: TestItem.md
[CancellationToken]: CancellationToken.md
[TestRunProfile]: TestRunProfile.md
[Uri]: Uri.md
[TestRunProfileKind]: TestRunProfileKind.md
[TestItemCollection]: TestItemCollection.md
[TestRun]: TestRun.md
[TestRunRequest]: TestRunRequest.md
[TestTag]: TestTag.md
