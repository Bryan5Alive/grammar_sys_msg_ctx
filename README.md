# Summary
This is an extension for Text generation web UI which parses the selected grammar_string for comments which it then appends to the custom_system_message.

# Explanation
Grammar files allow you to define how the AI bot sends data. You can make it only reply with JSON or XML or Emojis and so on with grammar.

For example you could make the AI only respond with:
```
name: ...
greeting: ...
```

Using the grammar:
```
root ::= name "\n" greeting

name ::= "name: " [A-Z][a-z]+
greeting ::= "greeting: " [^\n]+
```

An example output from the bot might be:
```
name: Olivia
greeting: Hello there, Bryan! How have you been lately? I'm Olivia, an AI designed to understand human emotions and communicate effectively with people like yourself. Feel free to share anything you like.
```

Obviously this can be very useful, however it becomes even more useful when coupled with instructions for the bot to follow. This extension allows you to add a comment block which will be injected into the system message so that the bot gives more predictable results.

For example, changing the grammar to:
```
root ::= name "\n" greeting

name ::= "name: " [A-Z][a-z]+
greeting ::= "greeting: " [^\n]+

# grammar_sys_msg:
# When generating a character name make it a fantasy witch name.
# When generating a character greeting make it cryptic.
# Example output:
# name: Helgathor
# greeting: Dreadful night to be out, isn't it?

```
(Note, the file must end in a blank line)

Here are some example outputs using this extension and the grammar above:
```
name: Xanthea
greeting: Shadows embrace thee, stranger. May the darkness hold no fear for thee.
```
```
name: Lyraeth
greeting: The stars align to guide you, my lost traveler.
```

As you can see the results are quite different with the provided instructions.

# Usage
Just make a grammar file and add a continuous block of comments starting with `# grammar_sys_msg:` like the example above. Again, make sure to add a blank line at the end.
