def return_debt_notice_template(username):
    return """<!DOCTYPE payloads PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<payloads
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  style="font-family: 'Poppins', 'helvetica neue', helvetica, sans-serif"
>
  <head>
    <meta charset="UTF-8" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta content="telephone=no" name="format-detection" />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap"
      rel="stylesheet"
    />
    <style type="text/css">
      #outlook a {
        padding: 0;
      }

      .es-button {
        mso-style-priority: 100 !important;
        text-decoration: none !important;
      }

      a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
      }

      .es-desk-hidden {
        display: none;
        float: left;
        overflow: hidden;
        width: 0;
        max-height: 0;
        line-height: 0;
        mso-hide: all;
      }

      [data-ogsb] .es-button {
        border-width: 0 !important;
        padding: 10px 20px 10px 20px !important;
      }

      @media only screen and (max-width: 600px) {
        p,
        ul li,
        ol li,
        a {
          line-height: 150% !important;
        }

        h1,
        h2,
        h3,
        h1 a,
        h2 a,
        h3 a {
          line-height: 120%;
        }

        h1 {
          font-size: 30px !important;
          text-align: left;
        }

        h2 {
          font-size: 24px !important;
          text-align: left;
        }

        h3 {
          font-size: 20px !important;
          text-align: left;
        }

        .es-header-payloads h1 a,
        .es-content-payloads h1 a,
        .es-footer-payloads h1 a {
          font-size: 30px !important;
          text-align: left;
        }

        .es-header-payloads h2 a,
        .es-content-payloads h2 a,
        .es-footer-payloads h2 a {
          font-size: 24px !important;
          text-align: left;
        }

        .es-header-payloads h3 a,
        .es-content-payloads h3 a,
        .es-footer-payloads h3 a {
          font-size: 20px !important;
          text-align: left;
        }

        .es-menu td a {
          font-size: 14px !important;
        }

        .es-header-payloads p,
        .es-header-payloads ul li,
        .es-header-payloads ol li,
        .es-header-payloads a {
          font-size: 14px !important;
        }

        .es-content-payloads p,
        .es-content-payloads ul li,
        .es-content-payloads ol li,
        .es-content-payloads a {
          font-size: 14px !important;
        }

        .es-footer-payloads p,
        .es-footer-payloads ul li,
        .es-footer-payloads ol li,
        .es-footer-payloads a {
          font-size: 14px !important;
        }

        .es-infoblock p,
        .es-infoblock ul li,
        .es-infoblock ol li,
        .es-infoblock a {
          font-size: 12px !important;
        }

        *[class="gmail-fix"] {
          display: none !important;
        }

        .es-m-txt-c,
        .es-m-txt-c h1,
        .es-m-txt-c h2,
        .es-m-txt-c h3 {
          text-align: center !important;
        }

        .es-m-txt-r,
        .es-m-txt-r h1,
        .es-m-txt-r h2,
        .es-m-txt-r h3 {
          text-align: right !important;
        }

        .es-m-txt-l,
        .es-m-txt-l h1,
        .es-m-txt-l h2,
        .es-m-txt-l h3 {
          text-align: left !important;
        }

        .es-m-txt-r img,
        .es-m-txt-c img,
        .es-m-txt-l img {
          display: inline !important;
        }

        .es-button-border {
          display: inline-block !important;
        }

        a.es-button,
        button.es-button {
          font-size: 18px !important;
          display: inline-block !important;
        }

        .es-adaptive table,
        .es-left,
        .es-right {
          width: 100% !important;
        }

        .es-content table,
        .es-header table,
        .es-footer table,
        .es-content,
        .es-footer,
        .es-header {
          width: 100% !important;
          max-width: 600px !important;
        }

        .es-adapt-td {
          display: block !important;
          width: 100% !important;
        }

        .adapt-img {
          width: 100% !important;
          height: auto !important;
        }

        .es-m-p0 {
          padding: 0px !important;
        }

        .es-m-p0r {
          padding-right: 0px !important;
        }

        .es-m-p0l {
          padding-left: 0px !important;
        }

        .es-m-p0t {
          padding-top: 0px !important;
        }

        .es-m-p0b {
          padding-bottom: 0 !important;
        }

        .es-m-p20b {
          padding-bottom: 20px !important;
        }

        .es-mobile-hidden,
        .es-hidden {
          display: none !important;
        }

        tr.es-desk-hidden,
        td.es-desk-hidden,
        table.es-desk-hidden {
          width: auto !important;
          overflow: visible !important;
          float: none !important;
          max-height: inherit !important;
          line-height: inherit !important;
        }

        tr.es-desk-hidden {
          display: table-row !important;
        }

        table.es-desk-hidden {
          display: table !important;
        }

        td.es-desk-menu-hidden {
          display: table-cell !important;
        }

        .es-menu td {
          width: 1% !important;
        }

        table.es-table-not-adapt,
        .esd-block-payloads table {
          width: auto !important;
        }

        table.es-social {
          display: inline-block !important;
        }

        table.es-social td {
          display: inline-block !important;
        }

        .es-desk-hidden {
          display: table-row !important;
          width: auto !important;
          overflow: visible !important;
          max-height: inherit !important;
        }
      }
    </style>
  </head>

  <payloads
    style="
      width: 100%;
      background-color: #161922;
      font-family: 'Poppins', 'helvetica neue', helvetica, sans-serif;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
      padding: 0;
      margin: 0;
    "
  >
    <div class="es-wrapper-color" style="background-color: #f6f6f6">
      <table
        class="es-wrapper"
        width="100%"
        cellspacing="0"
        cellpadding="0"
        style="
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
          border-collapse: collapse;
          border-spacing: 0px;
          padding: 0;
          margin: 0;
          width: 100%;
          height: 100%;
          background-repeat: repeat;
          background-position: center top;
          background-color: #f6f6f6;
        "
      >
        <tr>
          <td valign="top" style="padding: 0; margin: 0">
            <table
              class="es-header"
              cellspacing="0"
              cellpadding="0"
              align="center"
              style="
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                border-collapse: collapse;
                border-spacing: 0px;
                table-layout: fixed !important;
                width: 100%;
                background-color: transparent;
                background-repeat: repeat;
                background-position: center top;
              "
            >
              <tr>
                <td
                  align="center"
                  bgcolor="#161922"
                  style="padding: 0; margin: 0; background-color: #161922"
                >
                  <table
                    class="es-header-payloads"
                    cellspacing="0"
                    cellpadding="0"
                    bgcolor="#ffffff"
                    align="center"
                    style="
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      border-collapse: collapse;
                      border-spacing: 0px;
                      background-color: #ffffff;
                      width: 600px;
                    "
                  >
                    <tr>
                      <td
                        align="left"
                        bgcolor="#161922"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-left: 20px;
                          padding-right: 20px;
                          padding-top: 30px;
                          background-color: #161922;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <br />
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#252831"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-left: 20px;
                          padding-right: 20px;
                          padding-top: 30px;
                          background-color: #252831;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 33px;
                                        color: #ffffff;
                                        font-size: 22px;
                                      "
                                    >
                                      <br />
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 33px;
                                        color: #ffffff;
                                        font-size: 22px;
                                      "
                                    >
                                      <strong>b</strong>Auth
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <hr
                                      style="
                                        border-top: 1px solid #ffffff;
                                        border-bottom: 1px;
                                        width: 260px;
                                      "
                                    />
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#252831"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                          background-color: #252831;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 24px;
                                        color: #ffffff;
                                        font-size: 16px;
                                        font-weight: 800;
                                      "
                                    >
                                      """+username+"""
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#252831"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                          background-color: #252831;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 23px;
                                        color: #ffffff;
                                        font-size: 15px;
                                      "
                                    >
                                      Saudações! <br />Seja bem-vindo(a)
                                      ao bauth!<br /><br />

                                      Estamos felizes por ter se juntado a
                                      nós.<br />
                                      Com sua conta bAuth você tem <br />
                                      acesso aos nossos queridos<br />
                                      <a
                                        style="
                                          color: #5093fe;
                                          text-decoration: none;
                                        "
                                        href="https://b2oard.web.app/"
                                        >b²ord</a
                                      >
                                      e
                                      <a
                                        style="
                                          color: #5093fe;
                                          text-decoration: none;
                                        "
                                        href="https://planejaconta.web.app/dashboard"
                                      >
                                        planejaconta</a
                                      >
                                      <br />
                                      <br />
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#252831"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                          background-color: #252831;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <span
                                      class="msohide es-button-border-2 es-button-border"
                                      style="
                                        border-style: solid;
                                        background: #5093fe;
                                        border-width: 0px 0px 2px 0px;
                                        display: inline-block;
                                        border-radius: 30px;
                                        width: auto;
                                        mso-hide: all;
                                      "
                                      ><a
                                        href="#"
                                        class="es-button es-button-1"
                                        style="
                                          mso-style-priority: 100 !important;
                                          text-decoration: none;
                                          -webkit-text-size-adjust: none;
                                          -ms-text-size-adjust: none;
                                          mso-line-height-rule: exactly;
                                          color: #ffffff;
                                          font-size: 16px;
                                          border-style: solid;
                                          border-color: #5093fe;
                                          border-width: 10px 20px 10px 20px;
                                          display: inline-block;
                                          background: #5093fe;
                                          border-radius: 5px;
                                          font-family: 'Poppins',
                                            'helvetica neue', helvetica, arial,
                                            sans-serif;
                                          font-weight: normal;
                                          font-style: normal;
                                          line-height: 19px;
                                          width: auto;
                                          text-align: center;
                                        "
                                        >Ir para bAuth</a
                                      ></span
                                    ><!--<![endif]-->
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#252831"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                          background-color: #252831;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 23px;
                                        color: #ffffff;
                                        font-size: 15px;
                                      "
                                    >
                                      O bAuth é o autenticador dos serviços da
                                      Btree.<br />
                                      Caso não reconheça esse acesso entre em
                                      contato<br />
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 23px;
                                        color: #ffffff;
                                        font-size: 15px;
                                      "
                                    >
                                      <br />
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 23px;
                                        color: #ffffff;
                                        font-size: 15px;
                                      "
                                    >
                                      <br />
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 23px;
                                        color: #333333;
                                        font-size: 15px;
                                        font-weight: 800;
                                      "
                                    >
                                      <strong>2023 - Btree</strong>
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 21px;
                                        color: #333333;
                                        font-size: 14px;
                                      "
                                    >
                                      <br />
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#161922"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                          background-color: #161922;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="center"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 21px;
                                        color: #ffffff;
                                        font-size: 14px;
                                      "
                                    >
                                      Todos os direitos reservados -
                                      btreedevs@gmail.com
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td
                        align="left"
                        bgcolor="#161922"
                        style="
                          padding: 0;
                          margin: 0;
                          padding-top: 20px;
                          padding-left: 20px;
                          padding-right: 20px;
                          background-color: #161922;
                        "
                      >
                        <table
                          cellspacing="0"
                          cellpadding="0"
                          width="100%"
                          style="
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            border-collapse: collapse;
                            border-spacing: 0px;
                          "
                        >
                          <tr>
                            <td
                              class="es-m-p0r"
                              valign="top"
                              align="center"
                              style="padding: 0; margin: 0; width: 560px"
                            >
                              <table
                                width="100%"
                                cellspacing="0"
                                cellpadding="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tr>
                                  <td
                                    align="left"
                                    style="padding: 0; margin: 0"
                                  >
                                    <p
                                      style="
                                        margin: 0;
                                        -webkit-text-size-adjust: none;
                                        -ms-text-size-adjust: none;
                                        mso-line-height-rule: exactly;
                                        font-family: 'Poppins', 'helvetica neue',
                                          helvetica, arial, sans-serif;
                                        line-height: 21px;
                                        color: #333333;
                                        font-size: 14px;
                                      "
                                    >
                                      <br />
                                    </p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
  </payloads>
</payloads>
"""