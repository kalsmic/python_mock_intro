# Simple introduction to Mocking in Python

# [Youtube Video](https://youtu.be/T7hjrVewnbQ)

## Added for comparison

mock return_value using patch in with context

```python
def test_add_two_mocked_return_value(self):
    with mock.patch('builtins.input', return_value=10):
        result = add_two()
        expected = 20
        self.assertEqual(expected, result)
```

mock return_value using patch as decorator

```python
@mock.patch('builtins.input')
def test_add_two_mocked_return_value(self, mock_input):
    mock_input.return_value=10
    result = add_two()
    expected = 20
    self.assertEqual(expected, result)
```

side_effect using patch in with context

```python
def test_add_two_mocked_side_effect(self):
    with mock.patch('builtins.input', side_effect=[7, 10]):
        result = add_two()
        expected = 17
        self.assertEqual(expected, result)
```

side_effect using patch as decorator

```python
@mock.patch('builtins.input')
def test_add_two_mocked_side_effect(self,mock_input):
    mock_input.side_effect = [7, 10]
    result = add_two()
    expected = 17
    self.assertEqual(expected, result)
```



