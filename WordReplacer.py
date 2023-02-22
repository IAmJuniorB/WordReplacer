class WordReplacment():

    def replace_words_in_a_string(self, sen=str, word_to_replace=str, word_replacer=str) -> str:
        """Replaces given words in a string with another word

        Args:
            sen (string, not optional): a string of a sentence you are going to replace words with. Defaults to str.
            word_to_replace (string, not optional): The word in your string you no longer want. Defaults to str.
            word_replacer (string, not optional): The word in a string that replaces word_to_replace. Defaults to str.

        Returns:
            str: Your new sentence with replaced words
        """
        print(sen.replace(word_to_replace, word_replacer))

wr = WordReplacment()

wr.replace_words_in_a_string("GitHub is a horrible site", "horrible", "Awesome")