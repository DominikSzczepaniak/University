import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TagBuilder {
    private String tagName;
    private TagBuilder parent;
    private StringBuilder body = new StringBuilder();
    private Map<String, String> attributes = new HashMap<>();
    private boolean isIndented = false;
    private int indentation = 4;
    private int depth = 0;

    public TagBuilder() {
        this.tagName = "";
    }

    public TagBuilder(String tagName, TagBuilder parent) {
        this.tagName = tagName;
        this.parent = parent;
        if (parent != null) {
            this.depth = parent.depth + 1;
            this.isIndented = parent.isIndented;
            this.indentation = parent.indentation;
        }
    }

    public TagBuilder setIsIndented(boolean isIndented) {
        this.isIndented = isIndented;
        return this;
    }

    public TagBuilder setIndentation(int indentation) {
        this.indentation = indentation;
        return this;
    }

    public TagBuilder addContent(String content) {
        body.append(content);
        return this;
    }

    public TagBuilder startTag(String tagName) {
        return new TagBuilder(tagName, this);
    }

    public TagBuilder endTag() {
        if (parent != null) {
            parent.addContent(this.toString());
        }
        return parent;
    }

    public TagBuilder addAttribute(String name, String value) {
        attributes.put(name, value);
        return this;
    }

    private String getIndentation() {
        return isIndented ? " ".repeat(depth * indentation) : "";
    }

    private String getAttributesString() {
        return attributes.entrySet().stream()
                .map(entry -> String.format("%s='%s'", entry.getKey(), entry.getValue()))
                .collect(Collectors.joining(" ", " ", ""));
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        String indent = getIndentation();

        if (!tagName.isEmpty()) {
            sb.append(indent).append("<").append(tagName).append(getAttributesString());

            if (body.length() > 0) {
                sb.append(">\n");
                sb.append(body.toString().indent(indentation * (depth + 1)));
                sb.append(indent).append("</").append(tagName).append(">\n");
            } else {
                sb.append("/>\n");
            }
        } else {
            sb.append(body.toString());
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        TagBuilder tag = new TagBuilder();
        tag.setIsIndented(true).setIndentation(4);
        tag.startTag("parent")
                .addAttribute("parentproperty1", "true")
                .addAttribute("parentproperty2", "5")
                .startTag("child1")
                .addAttribute("childproperty1", "c")
                .addContent("childbody")
                .endTag()
                .startTag("child2")
                .addAttribute("childproperty2", "c")
                .addContent("childbody")
                .endTag()
                .endTag()
                .startTag("script")
                .addContent("$.scriptbody();")
                .endTag();

        System.out.println(tag.toString());
    }
}



class TagBuilderTest {

    @Test
    public void testTagBuilderIndentation() {
        TagBuilder tag = new TagBuilder();
        tag.setIsIndented(true).setIndentation(4);
        String expected = "    <parent parentproperty1='true' parentproperty2='5'>\n" +
                "                <child1 childproperty1='c'>\n" +
                "                    childbody\n" +
                "                </child1>\n" +
                "                <child2 childproperty2='c'>\n" +
                "                    childbody\n" +
                "                </child2>\n" +
                "    </parent>\n" +
                "    <script >\n" +
                "        $.scriptbody();\n" +
                "    </script>\n";
        tag.startTag("parent")
                .addAttribute("parentproperty1", "true")
                .addAttribute("parentproperty2", "5")
                .startTag("child1")
                .addAttribute("childproperty1", "c")
                .addContent("childbody")
                .endTag()
                .startTag("child2")
                .addAttribute("childproperty2", "c")
                .addContent("childbody")
                .endTag()
                .endTag()
                .startTag("script")
                .addContent("$.scriptbody();")
                .endTag();

        assertEquals(expected.trim(), tag.toString().trim());
    }
}

