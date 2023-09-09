# TestRunRequest

A TestRunRequest is a precursor to a TestRun, which in turn is created by passing a request to createTestRun. The TestRunRequest contains information about which tests should be run, which should not be run, and how they are run (via the profile).

In general, TestRunRequests are created by the editor and pass to runHandler, however you can also create test requests and runs outside of the runHandler.

## Constructors

```typescript
new TestRunRequest(include?: readonly TestItem[], exclude?: readonly TestItem[], profile?: TestRunProfile, continuous?: boolean): TestRunRequest
```

## Properties

### continuous

```typescript
continuous?: boolean
```

### exclude

```typescript
exclude: readonly TestItem[]
```

### include

```typescript
include: readonly TestItem[]
```

### profile

```typescript
profile: TestRunProfile
```

