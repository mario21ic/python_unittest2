from page_objects import PageObject, PageElement

class HomePage(PageObject):
    txtDescription = PageElement(id_='txtDescription')
    btnBuscar = PageElement(css='.btn.btn_cuaternary.tracking')

    linkLogin = PageElement(css='.menu_item_link.second > .login_init')
    txtUser = PageElement(id_='txtUser')
    txtPassword = PageElement(id_='txtPasswordLogin')
    btnLogin = PageElement(css='#frmUserLogIn .btn.btn_tertiary.mt10')

    def login_postulante(self, usuario, clave):
        self.linkLogin.click()
        self.txtUser = usuario
        self.txtPassword = clave
        self.btnLogin.click()
