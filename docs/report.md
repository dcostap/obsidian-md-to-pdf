# Title: Office & Licencias

Obsidian image link syntax: 
![[img1.png]]

## Subsection: Paths & Underscores

`U:\Informatica\VODAFONE\VARIOS\Clientes_CISCO.xlsx`

An empty link: []() here's an empty link


```python
import os

print("Hello, world!")

if __name__ == "__main__":
    print("This is the main function.")
```

Some text with underscores in normal context:  
_this_ _is_ text with more underscores: _foo_bar_

**BOLD TEXT**
_ITALICS TEXT_
*ITALICS WITH ASTERISKS*

these _words_ _are_ _in_ _italics_

Some bullet points:
- Item A_1
- Item A_2
- Item A_3 (ends with an underscore_)

A reference-style link: [Check this out][ref1]

## Footnotes

We have a footnote here[^footnote1] to test extra syntax. Another footnote over here[^footnote2].

## Another Section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit nulla ac augue consectetur, vitae rutrum nulla malesuada. Suspendisse nec justo vitae metus eleifend scelerisque.  
Praesent consequat nisl sit amet erat euismod, vel feugiat risus congue. Donec non mollis ipsum, non consequat enim. Morbi sodales, nibh non commodo iaculis, erat purus imperdiet felis, quis auctor neque ex eu arcu.

Cras ornare dolor non quam varius, a dignissim turpis malesuada. Maecenas ornare ante in libero porta, at rhoncus diam volutpat. Donec sodales finibus ex, et viverra sem commodo nec. Integer quis risus auctor, vehicula arcu nec, porta arcu.

### Sub-Heading With a Table

| Name       | ID    | Office Key         |
|------------|-------|--------------------|
| user_a     | 123   | _fake_key_1        |
| user_b     | 456   | VODA\_office\_2013 |
| someone_42 | 789   | ABC\_XYZ           |

This table includes underscores in cell content. Another footnote reference here[^footnote3].

### References to External Documents

For configuration details, refer to [DOC_sistemas][ref2]. Also see [DOC_inventario][ref3].  
We can also embed an image placeholder:
![[img2.png]]

Another image, inline: ![[img3.png]]

## A Final Section

Sed at fermentum nunc. Donec vitae porttitor dui. Maecenas vel sem venenatis, luctus velit eget, congue ipsum. Phasellus iaculis libero id lacus ornare posuere. Vestibulum imperdiet nulla ut venenatis facilisis. Aliquam porttitor sem viverra mi vulputate sollicitudin. Fusce suscipit, orci id sollicitudin fermentum, orci nibh dignissim libero, id semper lorem urna quis massa.

Another line referencing footnote[^footnote2]. Repeated references, just for testing.

## References

[ref1]: https://example.com "Example Link"
[ref2]: https://internal.server.com/doc_sistemas
[ref3]: https://internal.server.com/doc_inventario

[^footnote1]: This is the first footnote text.
[^footnote2]: A second footnote with some extra detail.
[^footnote3]: A third footnote referencing the table data.
