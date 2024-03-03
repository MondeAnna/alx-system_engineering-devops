### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* GCC:      9.4.0
* Ubuntu:   20.04 LTS

<br />

#### Requirements

* The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
* All your regex must be built for the Oniguruma library

<br />

#### Resources

* _[Regular-Expresions Info](https://www.regular-expressions.info/)_
* _[Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)_
* _[Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)_
* _[Rubular is your best friend](https://rubular.com/)_
* _[Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)_
* _[Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)_

<br />

#### Background Context

For this project, you have to build your regular expression using _[Oniguruma](https://www.rubydoc.info/gems/oniguruma/1.1.0)_, a regular expression library used by _[Ruby](https://www.ruby-lang.org/en/)_ by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the _Ruby_ code that you should use, just replace the regexp part, meaning the code in between the `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

<br />

#### SysEng and DevOps Projects

* _[`Match School`](0-simply_match_school.rb)_

<br />
