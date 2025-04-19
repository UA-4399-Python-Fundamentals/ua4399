philosophy = "The Zen of Python, by Tim Peters \
\n1.Beautiful is better than ugly. \
\n2.Explicit is better than implicit. \
\n3.Simple is better than complex. \
\n4.Complex is better than complicated. \
\n5.Flat is better than nested. \
\n6.Sparse is better than dense. \
\n7.Readability counts. \
\n8.Special cases aren\'t special enough to break the rules. \
\n9.Although practicality beats purity. \
\n10.Errors should never pass silently. \
\n11.Unless explicitly silenced. \
\n12.In the face of ambiguity, refuse the temptation to guess. \
\n13.There should be one-- and preferably only one --obvious way to do it. \
\n14.Although that way may not be obvious at first unless you\'re Dutch. \
\n15.Now is better than never. \
\n16.Although never is often better than *right* now. \
\n17.If the implementation is hard to explain, it\'s a bad idea. \
\n18.If the implementation is easy to explain, it may be a good idea. \
\n19.Namespaces are one honking great idea -- let\'s do more of those! \
\n20.Beautiful is better than ugly. \
\n21.Explicit is better than implicit. \
\n22.Simple is better than complex. \
\n23.Complex is better than complicated. \
\n24.Flat is better than nested. \
\n25.Sparse is better than dense. \
\n26.Readability counts. \
\n27.Special cases aren\'t special enough to break the rules. \
\n28.Although practicality beats purity. \
\n29.Errors should never pass silently. \
\n30.Unless explicitly silenced. \
\n31.In the face of ambiguity, refuse the temptation to guess. \
\n32.There should be one-- and preferably only one --obvious way to do it. \
\n33.Although that way may not be obvious at first unless you\'re Dutch. \
\n34.Now is better than never. \
\n35.Although never is often better than *right* now. \
\n36.If the implementation is hard to explain, it\'s a bad idea. \
\n37.If the implementation is easy to explain, it may be a good idea. \
\n38.Namespaces are one honking great idea -- let\'s do more of those!Beautiful is better than ugly. \
\n39.Explicit is better than implicit. \
\n40.Simple is better than complex. \
\n41.Complex is better than complicated. \
\n42.Flat is better than nested. \
\n43.Sparse is better than dense. \
\n44.Readability counts. \
\n45.Special cases aren\'t special enough to break the rules. \
\n46.Although practicality beats purity. \
\n47.Errors should never pass silently. \
\n48.Unless explicitly silenced. \
\n49.In the face of ambiguity, refuse the temptation to guess. \
\n50.There should be one-- and preferably only one --obvious way to do it. \
\n51.Although that way may not be obvious at first unless you\'re Dutch. \
\n52.Now is better than never. \
\n53.Although never is often better than *right* now. \
\n54.If the implementation is hard to explain, it\'s a bad idea. \
\n55.If the implementation is easy to explain, it may be a good idea. \
\n56.Namespaces are one honking great idea -- let\'s do more of those!"

betterWord = philosophy.count("better")
neverWord = philosophy.count("never")
isWord = philosophy.count("is")

print(f"Word 'better': {betterWord} times; 'never': {neverWord}; 'is': {isWord}")
print(philosophy.upper())