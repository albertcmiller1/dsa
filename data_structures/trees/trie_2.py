# words = ["foo", "food"]
words = ["a","b"]

trie_head = {}
for word in words:
    cur = trie_head
    for letter in word:
        cur = cur.setdefault(letter, {})
    cur['#'] = word

print(trie_head)
'''
The setdefault() method returns the value of the item with the specified key.
If the key does not exist, insert the key, with the specified value, see example below
{
    'f': {
        'o': {
            'o': {
                '#': 'foo', 
                'd': {
                    '#': 'food'
                }
            }
        }
    }
}
'''
