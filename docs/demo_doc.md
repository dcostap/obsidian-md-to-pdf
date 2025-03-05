# HEADING 1: TEST

## Subsection: Paths & Underscores

`U:\Test\Folders\Path\VARIOS\Clientes_CISCO.xlsx`

An empty link: []()

Normal link with alias: [Link to Google](https://www.google.com)

Normal link without alias: [https://www.google.com]()

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

ordered list:
1. Item 1
2. Item 2
3. Yet another item



## Footnotes

We have a footnote here[^footnote1] to test extra syntax. Another footnote over here[^footnote2].

[^footnote1]: This is the first footnote text.
[^footnote2]: A second footnote with some extra detail.

## Another Section

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit nulla ac augue consectetur, vitae rutrum nulla malesuada. Suspendisse nec justo vitae metus eleifend scelerisque.  
Praesent consequat nisl sit amet erat euismod, vel feugiat risus congue. Donec non mollis ipsum, non consequat enim. Morbi sodales, nibh non commodo iaculis, erat purus imperdiet felis, quis auctor neque ex eu arcu.

Cras ornare dolor non quam varius, a dignissim turpis malesuada. Maecenas ornare ante in libero porta, at rhoncus diam volutpat. Donec sodales finibus ex, et viverra sem commodo nec. Integer quis risus auctor, vehicula arcu nec, porta arcu.

### Sub-Heading With a Table


| Name   | ID  | Office Key  |
| ------ | --- | ----------- |
| user_a | 123 | _fake_key_1 |
| test   | 222 | 2222        |


| Name       | ID  | Office Key         |
| ---------- | --- | ------------------ |
| user_a     | 123 | _fake_key_1        |
| user_b     | 456 | VODA\_office\_2013 |
| someone_42 | 789 | ABC\_XYZ           |

This last table includes underscores in cell content. Another footnote reference here[^footnote3].

[^footnote3]: A third footnote referencing the table data.

# Images test

## Inline image links with text contents before

A small image, inline right after this text: ![[img3.png|alias text content for this image]]

Don't place big or important images like this.

## Image link right after text, in a newline

Newline small image, this text can be its description. 
![[img3.png|alias text content for this image]]

Don't place big or important images like this.

## Image links with blank newlines surrounding them

LaTeX will center these images horizontally, and show the alias text below each one. LaTeX may place the images in a separate new page if they don't fit nicely. Thus, you must always refer to these images from text via refs. Since I'm using `pandoc-crossref`, the link and Figure name are generated automatically when I use the reference link syntax:

Big image follows this text after two newlines. Link via reference label: [@fig:label_1]

![[img1.png|big image]]{#fig:label_1}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit nulla ac augue consectetur, vitae rutrum nulla malesuada. Suspendisse nec justo vitae metus eleifend scelerisque.

Now, linking to previous image again: [@fig:label_1]


Small image follows this text after two newlines. [@fig:label_2]

![[img3.png|small image]]{#fig:label_2}

# A Final Section

Sed at fermentum nunc. Donec vitae porttitor dui. Maecenas vel sem venenatis, luctus velit eget, congue ipsum. Phasellus iaculis libero id lacus ornare posuere. Vestibulum imperdiet nulla ut venenatis facilisis. Aliquam porttitor sem viverra mi vulputate sollicitudin. Fusce suscipit, orci id sollicitudin fermentum, orci nibh dignissim libero, id semper lorem urna quis massa.

Another line referencing footnote[^footnote2]. Repeated references, just for testing.

## Others


A quote block:

> The Isle of Elanor is an open-ended role-playing game, featuring a High Fantasy theme and setting.
> Branching Story Lines
> Character Building
> Factional Alignment
> Character Progression
> Combat Mechanics and Variety
> Consequences
> [The Isle of Elanor](https://www.commonwombat.com/blog)

