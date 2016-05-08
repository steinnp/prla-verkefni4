s = r"""^
(?P<title>[-\w'"]+(?P<separator>[ .])(?:[-\w'"]+\2)*?)
(?:(?:
        (?:
                  (?!\d+\2)
                            (?:s(?:eason\2?)?)
                                      (?P<season>(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3}))
                                                (?:\s{0,4})
                                                          (?:(?: e (?: pisode\2?)?))?
                                                                    (?P<episode>\d\d?)?
                                                                              (?:e\d\d?(?:-e?\d\d?)?\d\d?)?
                                                                                      )
            )
)"""
print(s.replace("\n","").replace(" ",""))
