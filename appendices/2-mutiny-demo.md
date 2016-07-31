\pagebreak

# Appendix 2: Mutiny demo application {-}

The following two code listings show the main body and spec file for the Mutiny demo application. The purpose of the one method provided is to return `true` if a supplied string is a palindrome, and `false` otherwise. A palindrome is a word that is unchanged when the order of its letters are reversed, for example "detartrate".

This demo application was created by Dr Louis Rose to provide an example codebase that would be supported by Mutiny. The full project repository (including the two files quoted below) is available at https://github.com/timw6n/mutiny-demo, which is itself a fork of https://github.com/mutiny/demo.

\usubsection{palindrome.rb}

```{.ruby}
module Demo
  class Palindrome
    def palindromic?(s)
      return true if s.size < 1
      first, *middle, last = s.chars
      first == last && palindromic?(middle.join)
    end
  end
end
```

\usubsection{palindrome\_spec.rb}

```{.ruby}
module Demo
  describe Palindrome do
    it "should accept the empty string" do
      expect(subject.palindromic?("")).to be_truthy
    end

    it "should accept a short palindrome" do
      expect(subject.palindromic?("aa")).to be_truthy
    end

    it "should accept a longer palindrome" do
      expect(subject.palindromic?("baab")).to be_truthy
    end

    it "should reject a short non-palindrome" do
      expect(subject.palindromic?("ab")).to be_falsey
    end

    it "should reject a longer non-palindrome" do
      expect(subject.palindromic?("babb")).to be_falsey
    end
  end
end
```
