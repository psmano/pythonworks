##getbook() eg.

import pyexcel


def test_add_book1(self):

    """

    test this scenario: book3 = book1 + book2
    """

    b1 = pyexcel.getbook(file_name=self.testfile)
    b2 = pyexcel.getbook(file_name=self.testfile2)
    b3 = b1 + b2
    content = b3.dict
    sheet_names = content.keys()
    assert len(sheet_names) == 6
    for name in sheet_names:
        if "Sheet3" in name:
            assert content[name] == self.content["Sheet3"]
        elif "Sheet2" in name:
            assert content[name] == self.content["Sheet2"]
        elif "Sheet1" in name:
            assert content[name] == self.content["Sheet1"]



