#!usr/bin/python
# -*- coding: latin-1 -*-
'''

    uirlis.py
    
    Program for plotting equations and modifying their parameters on the fly,
    as well as their plotting options. 
    The equations can be defined by the user by means of small text files with
    metaprogramming and python language methods. Examples are provided in the 
    folder whose name is stored in uirlis.cfg config file.
    
    Programa para graficar ecuaciones y modficar sus parámetros inmediatamente,
    así como también sus representaciones gráficas.
    Las ecuaciones pueden ser definidas mediante el usuario a través de pequeños 
    archivos de texto con metaprogramación y métodos en lenguaje python. Los 
    ejemplos provistos están en la carpeta cuyo nombre está guardado en el archivo
    de configuración uirlis.cfg.
    
    
    Copyright (C) 2016  Gustavo E. Carr
    

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.




                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {one line to give the program's name and a brief idea of what it does.}
    Copyright (C) {year}  {name of author}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
'''

import os
import csv                      # reading and writing .csv files.

import string
import numpy as np

import pygtk
pygtk.require('2.0')

import gtk                 # pygtk version: Maik Hertha <maik.hertha@berlin.de>


import matplotlib as mpl

mpl.use('GTKAgg')

import matplotlib.pyplot as plt

from matplotlib.figure import Figure

from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

# import the navigation toolbar.
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar

# para importar clases de ecuaciones.
from os import listdir
import imp, sys


# ----------------------------------- Pickle modules
import pickle

# --------------------------------------------- clase Controller.
class Controller(object):
    def __init__(self):

        print "Controlador funcionando.    Instanciando la vista."

        gtkWindow = gtk.Window()

        self.Id = 'Controller'
        self.counter = 0

        self.elementsList = dict()  # clave: Id, valor:puntero a cada objeto.

        self.setupView = SetupView()    # clase para setear los atributos de la vista gráfica.
        self.setupView.set_Id("setupView")
        self.setupView.set_name("setupView")
        self.setupView.set_type(str(type(self.setupView)).strip())
        self.setupView.set_parent(self)

        self.view = View(gtkWindow, Id='View', setupView=self.setupView)
        self.view.set_parent(self)      # la vista conoce al controlador.
        self.view.set_parentId(self.get_Id())   # se le pone el nombre del parent.

        self.view.set_Id("View")

        self.add_element(self.setupView)

        self.elementTypeDict = dict()
        self.elementTypeDict["<class '__main__.DataSeries'>"] = DataSeries
        self.elementTypeDict["<class '__main__.SetupView'>"] = SetupView

        self.elementTypeDictNames = dict()                  # acá entran los carteles que van a pantalla para crear ecuaciones.

        self.dataSeries = dict()

        self.dict_setters = dict(elementsList = self.set_elementsList)
        self.dict_getters = dict(elementsList = self.get_elementsList)

        self.filew = None
        
        self.creatorsDir = '.'
        self.initialMessage = ''
        
        self.initial_setup()

        self.init_creators()    # método para escanear módulos de creación de ecuaciones.
        
        return None


    def get_view(self):
        return self.view


    def get_setupView(self):
        return self.setupView


    def set_elementsList(self, elementsList):
        self.elementsList = elementsList
        return None

    def get_elementsList(self):
        return self.elementsList


    def set_elementTypeDict(self, elementTypeDict):
        self.elementTypeDict = elementTypeDict
        return None

    def get_elementTypeDict(self):
        return self.elementTypeDict


    def set_elementTypeDictNames(self, elementTypeDictNames):
        self.elementTypeDictNames = elementTypeDictNames
        return None

    def get_elementTypeDictNames(self):
        return self.elementTypeDictNames


    def get_dict_getters (self) :
        return self.dict_getters


    def get_dict_setters (self) :
        return self.dict_setters


    def initial_setup(self):
        
        archivo = ArchivoDeEntrada('Uirlis.cfg')
        lines = archivo.get_lines()
        
        dir = ''
        title = 'Uirlis.py'
        for line in lines:
            if ('@models_dir' in line) and ('=' in line):
                tag, rawdir = line.split('=')
                dir = rawdir.strip()
            if ('@appTitle' in line) and ('=' in line):
                tag, rawtitle = line.split('=')
                title = rawtitle.strip()
                self.get_view().set_appTitle(title)
        
        if dir != '':
            self.set_creatorsDir(dir)
        
        return None


    def init_creators(self):

        creators = self.get_elementTypeDict()
        typeNames = self.get_elementTypeDictNames()
        
        mypath = self.get_creatorsDir()
        
        try:
            f = listdir(mypath)
        except:            
            message = "\nNo se encontró el directorio de ecuaciones.\nRevisar el archivo de configuración Uirlis.cfg."
            self.get_view().set_initialMessage(message)
            return None

        # carga dinámica de módulos de modelos de ecuaciones.
        moduleNames = []

        for item in f:
            if (item.endswith('.py')) or (item.endswith('.mmm')):    moduleNames.extend([item])
            
        print 
        print ' Module names found:' ,moduleNames
        print

        for item in moduleNames:
            nombre, extension = item.split('.')

            # leemos el archivo entero y lo metemos en el string 'code'.
            print '----------------------------------------------'
            print 'Leyendo archivo: ',mypath+'/'+nombre+'.'+extension
            
            archivo = ArchivoDeEntrada(filename = mypath+'/'+nombre+'.'+extension)
            lines = archivo.get_lines()
            texto = ""
            for linea in lines:
                texto += linea
                        
            if extension == 'mmm':  # hay que crear el código dinámicamente.
                print 'extensión .mmm: creando texto de código.' 
                escritorDeClases = ModelClassWriter(lines, debug = True)
                
                escritorDeClases.write(debug = True)
                
                code = escritorDeClases.get_codeText()
                print '# -------------- Code for ',nombre
                print code
                print '# -------------- End of code for ',nombre
            else:
                print 'extensión .py: cargando el módulo directamente.' 
                code = texto

            print 'nombre =',nombre,'   type(nombre)=',type(nombre)
            print
            
            try:
                tipo, Creador, nombreClase = self.__importCode(code, nombre)
                print '         salida de Controller.__importCode():  tipo=',tipo,' (tipo:  ',type(tipo),'), Creador=',Creador,', nombre=',nombreClase
    
                if not(tipo == None):
    
                    typeNames[nombreClase] = tipo
                    creators[tipo] = Creador
            except:
                print 'Hubo error con la creación de módulo a partir de ',mypath+'/'+nombre+'.'+extension

            print '----------------------------------------------'

                
            print
            print 



        self.set_elementTypeDict(creators)
        self.set_elementTypeDictNames(typeNames)

        print '---'
        print 'creators =',creators
        print '---'
        print 'typeNames =', typeNames

        return None


    def __importCode(self, code, name, add_to_sys_modules=0):
        """
        source: http://code.activestate.com/recipes/82234-importing-a-dynamically-generated-module/

        Import dynamically generated code as a module. code is the
        object containing the code (a string, a file handle or an
        actual compiled code object, same types as accepted by an
        exec statement). The name is the name to give to the module,
        and the final argument says wheter to add it to sys.modules
        or not. If it is added, a subsequent import statement using
        name will return this module. If it is not added to sys.modules
        import will try to load it in the normal fashion.

        import foo

        is equivalent to

        foofile = open("/path/to/foo.py")
        foo = importCode(foofile,"foo",1)

        Returns a newly generated module.
        """
        import sys,imp

        print
        print '    en Controller.__importCode(), tratando de importar código de ', name, ':...'

        module = imp.new_module(name)

        exec code in module.__dict__

        #~ if add_to_sys_modules:
        sys.modules[name] = module

        try:
            Creador =  module.Model
            print '     type(Creador):',type(Creador), '  es :',Creador
        except:
            print '...no se instanció el modelo del módulo.'
            return None, None, None
        try:
            modeloDummy = Creador()                 # este es el creador de instancias de ecuación, son los valores del diccionario  self.elementTypeDict.
        except:
            print '...no se creó el modeloDummy.'
            return None, None, None
        try:
            tipo = str(type(modeloDummy)).strip()               # esta es la clave del diccionario  self.elementTypeDict, y  el valor del dict:  self.elementTypeDictNames.
            print 'en __importCode():  ',type(tipo)
        except:
            print '...no se obtuvo el tipo de modeloDummy como string.'
            return None, None, None
        try:
            nombre = modeloDummy.get_model_name()   # esta es la clave del diccionario  self.elementTypeDictNames.
        except:
            print '...no se obtuvo el nombre, modeloDummy.get_model_name(), del modelo del modeloDummy.'
            return None, None, None
        try:
            del modeloDummy
        except:
            print '...no se borró el objeto modeloDummy.'
            return None, None, None

        return tipo, Creador, nombre



    def set_creatorsDir(self, filename):
        self.creatorsDir = filename
        return None

    def get_creatorsDir(self):
        return self.creatorsDir


    # métodos para guardar.
    def set_saveFilename(self, filename):
        self.saveFilename = filename
        return None

    def get_saveFilename(self):
        return self.saveFilename


    def set_filew(self, filename):
        self.filew = filename
        return None

    def get_filew(self):
        return self.filew



    def get_modelsList(self):
        elementsList = self.get_elementsList()
        modelsList = dict()
        for item in elementsList:
            try:
                if elementsList[item].is_equation():
                    modelsList[item] = elementsList[item]
            except:
                pass
        return modelsList


    def add_element(self, element):
        ok = self.__validateElement(element)
        if ok:  # no está
            self.inc_counter()
            elementsList = self.get_elementsList()
            elementsList[element.get_Id()] = element

        return ok


    def del_element(self, element):
        ok = not(self.__validateElement(element))
        if ok:  # está
            elementsList = self.get_elementsList()
            del elementsList[element.get_Id()]
            self.set_elementsList(elementsList)
        return ok


    def __validateElement(self, element):
        elements = self.get_elementsList()
        #~ print 'En __validateElement():'
        #~ print 'elementsList=', elements

        #~ print '         Elemento a validar: element.get_Id()=', element.get_Id()

        elementFound = False
        for Id in elements.keys():

            nombre = elements[Id].get_name()
            #~ print '         Id de elemento en la lista de existentes=',Id,'  nombre=',nombre

            if Id == element.get_Id():  elementFound = True
            if nombre == element.get_name() and type(elements[Id])==type(element):
                elementFound = True
        return not(elementFound)


    def create_element(self, elementType=None, name=None):
        if (name == None) or (name == ""):
            nombre=str(self.get_counter())
        else:
            nombre = name

        modelCreators = self.get_elementTypeDict()
        Creator = modelCreators[elementType]
        print '   tipo del creador:',type(Creator)

        element = Creator(name=nombre, parent=self)

        element.set_Id(str(type(element))+str(self.get_counter()))
        element.set_debug(False)

        #~ ok = self.add_model(element)
        ok = self.add_element(element)

        print "Ok=",ok
        if not(ok):
            #~ print 'Borrando elemento...'
            del element
            return None
        else:
            return element


    def set_dataSeries(self, dataSeries):
        self.dataSeries = dataSeries
        return None

    def get_dataSeries(self):

        elementsList = self.get_elementsList()
        dataSeries = dict()
        #~ print " en get_dataSeries(): "
        #~ print "       elementsList =  ", elementsList
        #~
        for key, element in elementsList.items():
            #~ element = elementsList[key]
            #~ print '    key', key, ' tipo de elemento: ',str(type(element)).strip(),', nombre=',element.get_name()
            if (str(type(element)).strip() == "<class '__main__.DataSeries'>"):
                dataSeries[key] = element
        return dataSeries



    def __validateDataSeries(self, dataSeries):

        dictSeries = self.get_dataSeries() # diccionario

        #~ if (dictSeries == None) or (dictSeries == dict()):
            #~ return None

        series = dictSeries.keys() # las series propiamente dichas

        names = []
        for item in series:
            names.append(item.get_name())

        return not(dataSeries.get_name() in names)


    def __validateArtist(self, artist):

        dictSeries = self.get_dataSeries() # diccionario

        if (dictSeries == None) or (dictSeries == dict()):
            return None

        artists = dictSeries.values()  # hay un sólo artista por cada dataSeries.

        return not(artist.get_label() in artists)


    def findDataSeriesByArtist(self, artista):

        dictDataSeries = self.get_dataSeries()
        #~
        #~ print
        #~ print ' en  findDataSeriesByArtist: dictDataSeries=' ,dictDataSeries

        dataSeries = None

        #~ print "                         Buscando artist.get_label()=",artista.get_label()
        #~ print "                         En el    for dataS, artistLabel in dictDataSeries.items():  "

        for Id, dataSeriesObject in dictDataSeries.items():

            #~ print '                             Id, dataSeriesObject: ', Id, ',', dataSeriesObject

            if artista == dataSeriesObject.get_artista(): dataSeries = dataSeriesObject

        return dataSeries



    def findArtistByModel(self, modelo):

        dictDataSeries = self.get_dataSeries()
        dataSeries = None

        for clave, valor in dictDataSeries.items():
            if valor.get_name() == modelo.get_name():  dataSeries = valor

        if dataSeries != None:

            artista = dataSeries.get_artista()

            return artista
        else:
            return None


    def get_Id(self):
        return self.Id

    def get_name(self):
        return "Controller"

    def get_counter(self):
        return self.counter

    def inc_counter(self):
        self.counter += 1
        return None


    def updateModel(self, modelo):
        print ' haciendo update de modelo: ', modelo.get_name()

        #~ print ' valor de aesmm en updateMddel del controller:',modelo.get_aesmm()
        try:
            x,y = modelo.eval(modelo.get_indepVar())

            self.updateDataSeries(self.findArtistByModel(modelo))
        except:
            print 'Algo salió mal en la evaluación del modelo.'
            self.get_view().messageDialog("Error in evaluation of equation. \n Please check sintaxis and/or \n variables used in it.")
            
        return None


    def updateDataSeries(self, artista):
        #~ print 'en updateDataSeries, que no hace nada.'

        if artista == None: # hay que plotearlo.
            pass

        dataSeries = self.findDataSeriesByArtist(artista)
        print 'en updateDataSeries:  dataSeries =' ,dataSeries

        modelsList = self.get_modelsList()
        print '         modelsList=',modelsList

        for Id, modelObject in modelsList.items():

            if dataSeries.get_name() == modelObject.get_name():   # Los nombres son únicos y coinciden los de cada dataSerie con su Modelo.

                try:
                    x,y = modelObject.eval(modelObject.get_indepVar())

                    dataSeries.set_data([x,y])
                    dataSeries.updateGraphPropertiesEditor()
                except:
                    self.get_view().messageDialog("Error in evaluation of equation. \n Please check sintaxis and/or \n variables used in it.")
            

        return None

#~ #~
    def updateGraphProperties(self):
        self.get_view().create_graph()
        return None


    def save_file_ok_sel(self, w, filew):

        self.set_filew(filew)

        print "File ok sel: %s" % self.filew.get_filename()
        self.set_saveFilename(self.filew.get_filename())

        print 'filename=',self.get_saveFilename()

        self.filew.destroy()

        allData = dict()

        elementos = self.get_elementsList() # devuelve un diccionario.
        print '================================================================================== Guardando a archivo de texto (etapa 1) ==========='
        print '== Lista de elementos: '
        for clave, objeto in elementos.items():
            print 'clave=',clave,'   objeto:',objeto,'   nombre=',objeto.get_name()
        print '================================================================================= Guardando a archivo de texto (etapa 2) ============'
        print ' Recorriendo elementos = self.get_elementsList() '
        for clave, objeto in elementos.items():

            allData[clave] = objeto.get_data_as_dict()
            #~ print '                     clave=',clave,',   objeto=',dic[clave]

        print
        print ' Diccionario a picklear:',allData

        fid = open(self.get_saveFilename(),'w+')
        pickle.dump(allData, fid, 0)
        fid.close()

        return None

    def limpiarTodo(self):

        #~ print  '========= método Controller.limpiarTodo(), en construcción ========='
        borrar = dict()
        elementTypeDict = self.get_elementTypeDict()
        for clave, valor in elementTypeDict.items():
            if clave == "<class '__main__.DataSeries'>":
                borrar["<class '__main__.DataSeries'>"] = self.get_view().delete_experimentalData
            else:   # es alguno de los modelos.
                try:
                    borrar[clave] = self.get_view().delete_equation
                except:
                    pass

        elementsList = self.get_elementsList()

        notebook = self.get_view().get_notebook()
        print 'El notebook tiene:'
        for item in notebook.get_children():
            del item

        #~ for I in range(len(notebook.get_children()):



        for clave, objeto in elementsList.items():
            print ' Objeto a borrar:', objeto, ', nombre:',objeto.get_name()
            try:
                borrar[str(type(objeto)).strip()](objeto)
            except:
                pass

        self.get_view().set_setupView(self.get_setupView())

        return None

    def retrieve(self, archivo):

        print 'En el controlador... se eligió cargar archivo de sesión: ', archivo
        print
        print  '========= método Controller.retrieve(), en construcción ========='

        fid = open(archivo,'r+')
        allData = pickle.load(fid)
        fid.close()

        print 'Data unpickled:  ',allData

        retorno = self.createElementFromDump(allData)

        print '  -- - - - - -- - - -  - '
        print ' retorno = ',retorno
        print '  -- - - - - -- - - -  - '

        #~ self.set_elementsList(retorno)
        for elem in retorno:
            #~ self.get_elementsList().append(elem)
            print
            print '   elemento en retorno:',elem
            self.add_element(elem)

            try:
                if elem.is_setup():
                    print 'Actualizando setup.'
                    elem.set_parent(self)
                    self.get_view().setup(elem)
                    self.get_view().update_graph()
            except:

                print 'Intentando crear editor de propiedades del elemento: ',elem.get_name(),', de tipo:',type(elem)
                if elem.is_equation():
                    self.get_view().create_equation(elem)
                else:
                    print 'Tipo de elemento que se creó al hacer retrieve: ',type(elem)
                    self.get_view().plot_dataSeries(elem)

        # acá tal vez sea conveniente que refresque la vista, por si los cambios en el setupView llegaron después de crear todas las series y ecuaciones.
        self.get_view().update_graph()  # otra vez.
        return


    def createElementFromDump(self, dic):

        print
        print 'Entrando en createElementFromDump'
        lista = []

        Creators = self.get_elementTypeDict()       # me da los creadores de elementos que hay.

        for objectId in dic.keys():
            dicDatos = dic[objectId]        #   devuelve un diccionario con las claves de los setters y los valores de cada dato.

            tipo = dicDatos['type']

            obj = Creators[tipo]()
            setters = obj.get_dict_setters()

            for clave in dicDatos:
                setters[clave](dicDatos[clave])

            obj.set_Id(objectId)

            lista.append(obj)
        #~ claves1 = dic.keys()                        # las claves del diccionario que entró.

        return lista

# ------------------------------------------------------------
#
#
#
#
# ------------------------------------------------------------ clase SetupView.
class SetupView(object):

    #~ def __init__(self, WIDTH  = 800, HEIGHT = 600, canvasSizeH = 450, canvasSizeV = 350, logX = True, logY = True, figureSizeH = 5, figureSizeV = 4, dpi = 100, majorgridb = True, majorgridbColor = '0.45', majorgridlinestyle = '-', minorgridb = True, minorgridbColor = '0.65', minorgridlinestyle = '-', xlabel = "DK  MPa·m^0.5", ylabel = "da/dN  [m/cycle]", xlim0 = 1., xlim1 = 100., ylim0 = 1.0e-13, ylim1 = 1.0e-4, type = None, name = ""):
    def __init__(self, WIDTH  = 800, HEIGHT = 600, canvasSizeH = 450, canvasSizeV = 350, logX = False, logY = False, figureSizeH = 5, figureSizeV = 4, dpi = 100, majorgridb = True, majorgridbColor = '0.45', majorgridlinestyle = '-', minorgridb = True, minorgridbColor = '0.65', minorgridlinestyle = '-', xlabel = "X", ylabel = "Y", xlim0 = 0., xlim1 = 1., ylim0 = 0., ylim1 = 1., type = None, name = ""):

        # ------------------- Diccionarios.
        self.dict_setters = dict(WIDTH = self.set_WIDTH,
                HEIGHT = self.set_HEIGHT,
                canvasSizeH = self.set_canvasSizeH,
                canvasSizeV = self.set_canvasSizeV,
                logX = self.set_logX,
                logY = self.set_logY,
                figureSizeH = self.set_figureSizeH,
                figureSizeV = self.set_figureSizeV,
                dpi = self.set_dpi,
                majorgridb = self.set_majorgridb,
                majorgridbColor = self.set_majorgridbColor,
                majorgridlinestyle = self.set_majorgridlinestyle,
                minorgridb = self.set_minorgridb,
                minorgridbColor = self.set_minorgridbColor,
                minorgridlinestyle = self.set_minorgridlinestyle,
                xlabel = self.set_xlabel,
                ylabel = self.set_ylabel,
                xlim0 = self.set_xlim0,
                xlim1 = self.set_xlim1,
                ylim0 = self.set_ylim0,
                ylim1 = self.set_ylim1,
                type = self.set_type)

        self.dict_getters = dict(WIDTH = self.get_WIDTH,
                HEIGHT = self.get_HEIGHT,
                canvasSizeH = self.get_canvasSizeH,
                canvasSizeV = self.get_canvasSizeV,
                logX = self.get_logX,
                logY = self.get_logY,
                figureSizeH = self.get_figureSizeH,
                figureSizeV = self.get_figureSizeV,
                dpi = self.get_dpi,
                majorgridb = self.get_majorgridb,
                majorgridbColor = self.get_majorgridbColor,
                majorgridlinestyle = self.get_majorgridlinestyle,
                minorgridb = self.get_minorgridb,
                minorgridbColor = self.get_minorgridbColor,
                minorgridlinestyle = self.get_minorgridlinestyle,
                xlabel = self.get_xlabel,
                ylabel = self.get_ylabel,
                xlim0 = self.get_xlim0,
                xlim1 = self.get_xlim1,
                ylim0 = self.get_ylim0,
                ylim1 = self.get_ylim1,
                type = self.get_type)

        # ------------------- Atributos
        self.WIDTH   = WIDTH
        self.HEIGHT  = HEIGHT
        self.canvasSizeH  = canvasSizeH
        self.canvasSizeV  = canvasSizeV
        self.logX  = logX
        self.logY  = logY
        self.figureSizeH  = figureSizeH
        self.figureSizeV  = figureSizeV
        self.dpi  = dpi
        self.majorgridb  = majorgridb
        self.majorgridbColor  = majorgridbColor
        self.majorgridlinestyle  = majorgridlinestyle
        self.minorgridb  = minorgridb
        self.minorgridbColor  = minorgridbColor
        self.minorgridlinestyle  = minorgridlinestyle
        self.xlabel  = xlabel
        self.ylabel  = ylabel
        self.xlim0 = xlim0
        self.xlim1 = xlim1
        self.ylim0 = ylim0
        self.ylim1 = ylim1
        self.type = type
        self.name = name
        self.hayQueReplotear = False
        #~ self.grafico = None     # a éste es al que se le cambian los atributos, es el de la vista.
        self.ventana = None
        self.entries = None
        self.parent = None
        
        self.debug = False

        # estas son todas las claves, en caso de usarse, hay que descomentar esta línea y comentarl la que sigue.
        #~ self.dict_UIkeys = ['xlabel', 'ylabel', 'xlim0', 'xlim1', 'ylim0', 'ylim1', 'WIDTH', 'HEIGHT', 'canvasSizeH', 'canvasSizeV', 'logX', 'logY', 'figureSizeH', 'figureSizeV', 'dpi', 'majorgridb', 'majorgridbColor', 'majorgridlinestyle', 'minorgridb', 'minorgridbColor', 'minorgridlinestyle']
        self.dict_UIkeys = ['xlabel', 'ylabel', 'xlim0', 'xlim1', 'ylim0', 'ylim1', 'logX', 'logY', 'dpi', 'majorgridb', 'majorgridbColor', 'majorgridlinestyle', 'minorgridb', 'minorgridbColor', 'minorgridlinestyle']

        self.dict_UIlabels = dict(WIDTH = 'Ancho de pantalla',
                                  HEIGHT = 'Alto de pantalla',
                                  canvasSizeH = 'Ancho del gráfico [in]',
                                  canvasSizeV = 'Alto del gráfico [in]',
                                  logX = 'Escala logarítimica en X [True|False]',
                                  logY = 'Escala logarítimica en Y [True|False]',
                                  figureSizeH = 'Ancho de la figura',
                                  figureSizeV = 'Alto de la figura',
                                  dpi = 'Definición (dots per inch)',
                                  majorgridb = 'Mostrar la grilla principal [True|False]',
                                  majorgridbColor = 'Color de la grilla principal',
                                  majorgridlinestyle = 'Tipo de línea de la grilla ppal',
                                  minorgridb = 'Mostrar la grilla secundaria [True|False]',
                                  minorgridbColor = 'Color de la grilla secundaria',
                                  minorgridlinestyle = 'Tipo de línea de la grilla secundaria',
                                  xlabel = 'Texto del eje X' ,
                                  ylabel = 'Texto del eje Y',
                                  xlim0 = 'Limite inferior del eje X',
                                  xlim1 = 'Limite superior del eje X',
                                  ylim0 = 'Limite inferior del eje Y',
                                  ylim1 = 'Limite superior del eje Y')

        return None

    # --------------------------------------------- Setters and getters
    # ----- dicts.
    def get_dict_getters(self):
        return self.dict_getters

    def get_dict_setters(self):
        return self.dict_setters

    def get_dict_UIkeys(self):
        return self.dict_UIkeys

    def get_dict_UIlabels(self):
        return self.dict_UIlabels

    def get_UIlabels(self):
        orden = self.get_dict_UIkeys()
        labelsTxt = []
        labels = self.get_dict_UIlabels()
        for item in orden:
             labelsTxt.append(labels[item])
        return labelsTxt

    # ----- attribs.
    def set_Id(self, Id):
        self.Id = Id
        return None

    def get_Id(self):
        return self.Id


    def set_name(self, name):           # este método se utiliza durante el uso normal del objeto.
        self.name = name
        return None

    def get_name(self):                 # este método se utiliza durante el uso normal del objeto.
        return self.name


    def set_type(self, type):
        self.type = type
        return None

    def get_type(self):
        return self.type


    def set_WIDTH(self, WIDTH):
        self.WIDTH = WIDTH
        return None

    def get_WIDTH(self):
        return self.WIDTH


    def set_HEIGHT(self, HEIGHT):
        self.HEIGHT = HEIGHT
        return None

    def get_HEIGHT(self):
        return self.HEIGHT


    def set_canvasSizeH(self, canvasSizeH):
        self.canvasSizeH = canvasSizeH
        return None

    def get_canvasSizeH(self):
        return self.canvasSizeH


    def set_canvasSizeV(self, canvasSizeV):
        self.canvasSizeV = canvasSizeV
        return None

    def get_canvasSizeV(self):
        return self.canvasSizeV


    def set_logX(self, logX):
        self.logX = logX
        self.set_hayQueReplotear(True)
        return None

    def get_logX(self):
        return self.logX


    def set_logY(self, logY):
        self.logY = logY
        self.set_hayQueReplotear(True)
        return None

    def get_logY(self):
        return self.logY


    def set_figureSizeH(self, figureSizeH):
        self.figureSizeH = figureSizeH
        return None

    def get_figureSizeH(self):
        return self.figureSizeH


    def set_figureSizeV(self, figureSizeV):
        self.figureSizeV = figureSizeV
        return None

    def get_figureSizeV(self):
        return self.figureSizeV


    def set_dpi(self, dpi):
        self.dpi = dpi
        return None

    def get_dpi(self):
        return self.dpi


    def set_majorgridb(self, majorgridb):
        self.majorgridb = majorgridb
        return None

    def get_majorgridb(self):
        return self.majorgridb


    def set_majorgridbColor(self, majorgridbColor):
        self.majorgridbColor = majorgridbColor
        return None

    def get_majorgridbColor(self):
        return self.majorgridbColor


    def set_majorgridlinestyle(self, majorgridlinestyle):
        self.majorgridlinestyle = majorgridlinestyle
        return None

    def get_majorgridlinestyle(self):
        return self.majorgridlinestyle


    def set_minorgridb(self, minorgridb):
        self.minorgridb = minorgridb
        return None

    def get_minorgridb(self):
        return self.minorgridb


    def set_minorgridbColor(self, minorgridbColor):
        self.minorgridbColor = minorgridbColor
        return None

    def get_minorgridbColor(self):
        return self.minorgridbColor


    def set_minorgridlinestyle(self, minorgridlinestyle):
        self.minorgridlinestyle = minorgridlinestyle
        return None

    def get_minorgridlinestyle(self):
        return self.minorgridlinestyle


    def set_xlabel(self, xlabel):
        self.xlabel = xlabel
        return None

    def get_xlabel(self):
        return self.xlabel


    def set_ylabel(self, ylabel):
        self.ylabel = ylabel
        return None

    def get_ylabel(self):
        return self.ylabel


    def set_xlim0(self, xlim0):
        self.xlim0 = xlim0
        return None

    def get_xlim0(self):
        return self.xlim0


    def set_xlim1(self, xlim1):
        self.xlim1 = xlim1
        return None

    def get_xlim1(self):
        return self.xlim1


    def set_ylim0(self, ylim0):
        self.ylim0 = ylim0
        return None

    def get_ylim0(self):
        return self.ylim0


    def set_ylim1(self, ylim1):
        self.ylim1 = ylim1
        return None

    def get_ylim1(self):
        return self.ylim1


    def set_parent(self, parent):
        self.parent = parent
        return None

    def get_parent(self):
        return self.parent


    def set_debug(self,debug):
        self.debug = debug
        return None

    def get_debug(self):
        return self.debug


    def set_ventana(self, ventana):
        self.ventana = ventana
        return None

    def get_ventana(self):
        return self.ventana


    def set_entries(self, entries):
        self.entries = entries
        return None

    def get_entries(self):
        return self.entries


    def set_hayQueReplotear(self, hayQueReplotear):
        self.hayQueReplotear = hayQueReplotear
        return None

    def get_hayQueReplotear(self):
        return self.hayQueReplotear

#~
    #~ def set_grafico(self, grafico):
        #~ self.grafico = grafico
        #~ return None
#~
    #~ def get_grafico(self):
        #~ return self.grafico


    # --------------------------------------------- Methods
    def is_setup(self):
        return True


    def is_equation(self):
        return False


    def run_dialog(self, applyLabel=gtk.STOCK_APPLY, okLabel=gtk.STOCK_OK, cancelLabel=gtk.STOCK_CANCEL):

        print 'en SetupView().'
        ventana = self.get_ventana()
        if ventana != None:
            print 'ventana=',ventana
            ventana.show()
            return None
        else:
            print 'ventana=',ventana


        getters = self.get_dict_getters()
        UIgetters = self.get_parent().get_view().get_dict_entryTypes()

        orden = self.get_dict_UIkeys()
        labelsIn = self.get_UIlabels()

        self.ventana = gtk.Window() #, None, 0,

        self.ventana.set_default_size(200, 200)

        #~ self.ventana.set_title(self.get_titulo())
        self.ventana.set_title("Edit setup ")
        self.ventana.connect("destroy", self.destroy)
        self.ventana.connect("delete-event", self.destroy)

        hbox = gtk.HBox(False, 4)
        hbox.set_border_width(4)
        self.ventana.add(hbox)


        table = gtk.Table(len(labelsIn)+1, 2)
        table.set_row_spacings(4)
        table.set_col_spacings(3)
        hbox.pack_start(table, True, True, 0)

        entries=[]
        labels=[]


        for I in range(len(orden)):

            #~ print 'I=',I, '  labelsIn[I]=',labelsIn[I]

            # label definition for entry.
            objLabel = gtk.Label(labelsIn[I])
            labels.append(objLabel)
            table.attach(objLabel,0,1,I,I+1)

            #~ print 'orden[I]=',orden[I],'|  UIgetters[orden[I]]=',UIgetters[orden[I]],'|  getter:',getters[orden[I]],'|  valor=',getters[orden[I]]()

            try:
                #~ print 'UIgetters[orden[I]] =',UIgetters[orden[I]]
                objEntry = UIgetters[orden[I]]()

                objEntry.set_value(getters[orden[I]]())     # acá asigna los valores a los objetos de entrada.

                objEntry.set_callback(self.on_modifCoef)

                entries.append(objEntry)
                table.attach(objEntry,1,3,I,I+1)

                objLabel.set_mnemonic_widget(objEntry)
            except:
                print "Object entry creation failure for key:", orden[I]


        self.set_entries(entries)

        applyButton = gtk.Button('Aplicar')
        applyButton.connect("clicked", self.on_apply)

        okButton = gtk.Button('OK')
        okButton.connect("clicked", self.on_ok)

        cancelButton = gtk.Button('Cancelar')
        cancelButton.connect("clicked", self.on_cancel)

        table.attach(applyButton,0,1,I+1,I+2)
        table.attach(okButton,1,2,I+1,I+2)
        table.attach(cancelButton,2,3,I+1,I+2)
        hbox.show_all()

        self.ventana.show_all()

        return None


    def on_apply(self, event):
        print 'apply'
        print 'self.get_parent()=',self.get_parent()

        # ---- Seteo de los parámetros de esta clase desde los datos en el diálogo.
        setters = self.get_dict_setters()
        UIgetters = self.get_parent().get_view().get_dict_entryTypes()

        entries = self.get_entries()

        orden = self.get_dict_UIkeys()

        for I in range(len(orden)):
            #~ print ' Entry:', entries[I],
            #~ print ', value:',entries[I].get_value()
            setters[orden[I]](entries[I].get_value())           # esto pone los valores de la gui en el modelo.
            #~ print '  poniendo valor:',entries[I].get_value(),' en setter :',orden[I],', método:',setters[orden[I]]
        # ----


        self.get_parent().get_view().update_graph()



        return None


    def on_ok(self, event):
        print 'En setupView.on_ok()'
        self.on_apply(event)
        self.destroy(event)
        return None


    def on_modifCoef(self):
        self.on_apply(None)
        return None


    def on_cancel(self, event):
        print 'Cancel'
        #~ dataSeries = self.get_dataSeries()
        #~ setters = self.get_dataSeries().get_dict_setters()
        #~ getters = dataSeries.get_dict_getters()
        #~
        #~ orden = dataSeries.get_dict_UIkeys()
        #~
        self.destroy(event)

        return None


    def destroy(self, event=None, dummy=None):

        self.get_ventana().destroy()
        self.set_ventana(None)

        return None


    def get_data_as_dict(self):

        self.dic = dict()
        getters = self.get_dict_getters()

        for clave in getters.keys():       # devuelve las claves o valores de los atributos en una lista.

            attrib = getters[clave]()       # devuelve el valor (u objeto) del getter.

            #~ print '   En elemento:',self.get_name(),'.   atributo:',attrib, 'tipo :',type(attrib)

            if type(attrib) == type([1,2]):
                #~ print 'es lista'
                lista = []
                for item in attrib:

                    #~ print '             en clase base Element, item de attrib:',item
                    try:
                        #~ print '   intentando pedir data as dict'
                        obj = item.get_data_as_dict()
                        lista.append(obj)

                    except:
                        #~ print '      no dio data as dict'
                        lista.append(item)

                self.dic[clave] = lista

            else:

                try:
                    obj = attrib.get_data_as_dict()
                    self.dic[clave] = obj
                    #~ print '              self.dic[clave] = obj:  self.dic[',clave,']=',obj

                except:
                    self.dic[clave] = attrib

        return self.dic

# --------------------------------------------- fin clase SetupView
#
#
#
#
# ================================= View
class View(object):
    def __init__(self, gtkWindow=None, Id=None, color = None, setupView=None, appTitle = 'Uirlis equations plotter'):

        if gtkWindow == None:
            return None

        print "Inicializando vista."

        self.dict_entryTypes = dict(name = TextEntry,
                                marker = TextEntry,
                                markersize = NumericEntry,
                                markeredgewidth = NumericEntry,
                                linestyle = TextEntry,
                                data = CellRendererSpinWindow,
                                visible = BoolEntry,
                                colour = ColourButton,
                                linewidth = TextEntry,
                                filled = TextEntry,
                                WIDTH  = NumericEntry,
                                HEIGHT = NumericEntry,
                                canvasSizeH = NumericEntry,
                                canvasSizeV = NumericEntry,
                                logX = BoolEntry,
                                logY = BoolEntry,
                                figureSizeH = NumericEntry,
                                figureSizeV = NumericEntry,
                                dpi = NumericEntry,
                                majorgridb = BoolEntry,
                                majorgridbColor = TextEntry,
                                majorgridlinestyle = TextEntry,
                                minorgridb = BoolEntry,
                                minorgridbColor = TextEntry,
                                minorgridlinestyle = TextEntry,
                                xlabel = TextEntry,
                                ylabel = TextEntry,
                                xlim0 = NumericEntry,
                                xlim1 = NumericEntry,
                                ylim0 = NumericEntry,
                                ylim1 = NumericEntry)

        self.dict_entryTypes[str(type("aa"))] = TextEntry
        self.dict_entryTypes[str(type(1.0))]= NumericEntry
        self.dict_entryTypes[str(type([1,2]))] = RangeEntry
        self.dict_entryTypes["<type 'numpy.ndarray'>"] = RangeEntry


        self.Id = Id
        self.gtkWindow = gtkWindow #~ gtk.Window.__init__(self)
        self.parent = None
        self.appTitle = appTitle

        self.session_filename = ""

        self.frameList = dict()
        self.lastPage = 0

        self.setupView = setupView

        self.ui_string = """<ui>
<menubar name='Menubar'>
    <menu action='FileMenu'>
          <menuitem action='New'/>
          <menuitem action='Open'/>
          <menuitem action='Save'/>      <separator/>
          <menuitem action='Quit'/>
    </menu>

    <menu action='ElementosMenu'>

          <menuitem action='NewRange'/>
          <menuitem action='EditRange'/>
          <menuitem action='DeleteRange'/>
    <separator/>

          <menuitem action='NewEquation'/>
          <menuitem action='EditEquation'/>
          <menuitem action='DeleteEquation'/>


    </menu>
    <menu action='HelpMenu'>
         <menuitem action='Debug'/>
         <menuitem action='About'/>
    </menu>
</menubar>
</ui>"""

        window = self.get_gtkWindow()   # la ventana principal está instanciada afuera y es pasada por parámetro.

        print "Creando ventana gráfica."

        self.WIDTH  = self.get_setupView().get_WIDTH()
        self.HEIGHT = self.get_setupView().get_HEIGHT()
        window.set_size_request(self.WIDTH, self.HEIGHT)

        window.connect('delete-event', self._on_delete_event)

        window.set_position(gtk.WIN_POS_CENTER)
        window.set_title(self.get_appTitle())

        window.main_vbox = gtk.VBox()
        window.add(window.main_vbox)

        window.main_vbox.show()

        uimgr = self._create_ui()
        uimgr.connect('connect-proxy', self._on_uimanager__connect_proxy)
        uimgr.connect('disconnect-proxy', self._on_uimanager__disconnect_proxy)

        menubar = uimgr.get_widget('/Menubar')
        window.main_vbox.pack_start(menubar, expand=False)
        menubar.show()

        window.show_all()

        self.table = gtk.Table(2, 2, gtk.FALSE)

        cajab = gtk.HPaned()
        cajab.show()
        window.surface = cajab

        self.table.attach(self.get_surface(), 0, 1, 0, 1, gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 0)

        window.main_vbox.pack_start(self.table)
        # ------------------------------------------------------

        # Status bar
        status = gtk.Statusbar()

        window.main_vbox.pack_end(status, expand=False)
        status.show()
        self.statusbar = status
        self._menu_cix = -1

        self.notebook = gtk.Notebook()
        self.notebook.set_tab_pos(gtk.POS_TOP)        #~ marcoEq = gtk.Frame("Ecuaciones")

        cajab.add1(self.get_notebook())

        marcoGraph = gtk.Frame("Gráfico")
        cajab.add2(marcoGraph)

        #~ self.WIDTH  = 1024
        #~ self.HEIGHT = 700

        self.COLOR = dict(
            bg  = "#BBCCFF"   , # ex "navajowhite"
            fg  = "darkblue"      ,
            txt = "#000"          ,
            white = 'white'         ,
            selected = '#67a3ce', )

        colormap = self.get_gtkWindow().get_colormap()
        self.COLOR = dict([(k,colormap.alloc_color(v)) for (k,v) in self.COLOR.items()])


        self.dictTypeWidget = dict()
        self.dictTypeWidget[str(type("abc"))] = TextEntry
        self.dictTypeWidget[str(type([1,2,3]))] = CellRendererSpinWindow
        self.dictTypeWidget[str(type(1.1))] = NumericEntry

        # acá dentro va todo el gráfico con barra de herramientas, etc.

        self.fig = None
        self.subp = None
        self.axes = None
        self.xlim0 = None
        self.xlim1 = None
        self.ylim0 = None
        self.ylim1 = None
        self.canvas = None
        
        self.debug = False

        self.initialMessage = ''    # initial warning message or whatever.

        #~ self.xlabelHandle = None
        #~ self.ylabelHandle = None

        self.update_graph()

        sw = gtk.ScrolledWindow()
        vboxg = gtk.VBox()               # crea una caja de apliado vertical.

        self.canvas.set_size_request(450,350)
        sw.add_with_viewport(self.canvas)


        vboxg.pack_start(sw, expand=1, fill=True)

        toolbar = NavigationToolbar(self.canvas, window)           # add navigation bar.
        
        # esto es para quitar todos los widgets de modificación salvo el botón "save", desde acá ---
        for I in range(0,8):
            widget = toolbar.get_nth_item(0)   # encuentra el ésimo elemento.
            widget.destroy()                   # destruye el widget.
            toolbar.update()
        # --- hasta acá.
        
        vboxg.pack_start(toolbar, expand=False, fill=False)   # add the NavigationToolbar to the box container
        # ----

        # ================ callbacks.
        self.get_fig().canvas.mpl_connect('button_press_event',self.onclick)
        self.get_fig().canvas.mpl_connect('pick_event',self.onpick)
        # ================ fin callbacks.

        marcoGraph.add(vboxg)
        
        print self.get_initialMessage()
        
        if self.get_initialMessage() != '': self.messageDialog(self.get_initialMessage())        
        
        window.show_all()
        
        print "-----"

        return None


    def get_dict_entryTypes(self):
        return self.dict_entryTypes


    def get_gtkWindow(self):
        return self.gtkWindow


    def get_ui_string(self):
        return self.ui_string


    def get_surface(self):
        return self.get_gtkWindow().surface


    def get_subp(self):
        return self.subp


    def set_frameList(self, frameList):
        self.frameList = frameList
        return None

    def get_frameList(self):
        return self.frameList


    def set_lastPage(self, lastPage):
        self.lastPage = lastPage
        return None

    def get_lastPage(self):
        return self.lastPage


    def get_notebook(self):
        return self.notebook


    def set_Id(self, Id):
        self.Id = Id
        return None

    def get_Id(self):
        return self.Id


    def set_parent(self, parent):
        self.parent = parent
        return None

    def get_parent(self):
        return self.parent


    def set_parentId(self, parentId):# este método se utiliza al deshidratar y rehidratar los objetos.
        self.parentId = parentId
        return None

    def get_parentId(self):          # este método se utiliza al deshidratar y rehidratar los objetos.
        return self.parentId


    def set_session_filename(self, session_filename):
        self.session_filename = session_filename
        return None

    def get_session_filename(self):
        return self.session_filename


    def set_initialMessage(self, initialMessage):
        self.initialMessage = initialMessage
        return None

    def get_initialMessage(self):
        return self.initialMessage


    def set_appTitle(self, appTitle):
        self.appTitle = appTitle
        win = self.get_gtkWindow()
        if win != None:
            win.set_title(appTitle)
        return None

    def get_appTitle(self):
        return self.appTitle


    def set_xlim0(self, xlim0):
        self.xlim0 = xlim0
        return None

    def get_xlim0(self):
        return self.xlim0


    def set_xlim1(self, xlim1):
        self.xlim1 = xlim1
        return None

    def get_xlim1(self):
        return self.xlim1


    def set_ylim0(self, ylim0):
        self.ylim0 = ylim0
        return None

    def get_ylim0(self):
        return self.ylim0


    def set_ylim1(self, ylim1):
        self.ylim1 = ylim1
        return None

    def get_ylim1(self):
        return self.ylim1


    def set_debug(self,debug):
        self.debug = debug
        return None

    def get_debug(self):
        return self.debug


    def set_fig(self, fig):
        self.fig = fig
        return None

    def get_fig(self):
        return self.fig


    def set_axes(self, axes):
        self.axes = axes
        return None

    def get_axes(self):
        return self.axes


    def set_canvas(self, canvas):
        self.canvas = canvas
        return None

    def get_canvas(self):
        return self.canvas


    def get_dictTypeWidget(self):
        return self.dictTypeWidget


    def set_setupView(self, setupView):
        self.setupView = setupView
        return None

    def get_setupView(self):
        return self.setupView


    def _create_ui(self):

        print "Creando menúes."

        window = self.get_gtkWindow()

        ag = gtk.ActionGroup('AppActions')

        ui = gtk.UIManager()

        actions = [
            ('FileMenu', None, '_File'),
            ('New',      gtk.STOCK_NEW , '_New session', '<control>N',
             'Create a new session', self._on_action_new),
            ('Open',     gtk.STOCK_OPEN, '_Open session', '<control>O',
             'Open or merge a session', self.retrieve), #~ 'Open a file', self._on_action_open),
            ('Save',     gtk.STOCK_SAVE, '_Save the current session', '<control>S',
             'Save this session', self.persist),    #'Save a file', self._on_action_save),
            ('Quit',     gtk.STOCK_QUIT, '_Quit application', '<control>Q',
             'Quit application', self._on_action_quit),
            ('EditMenu', None, 'E_dit'),
            ('Undo',      gtk.STOCK_UNDO , '_Undo', '<control>Z',
             'Undo last actions', None),
            ('Redo',      gtk.STOCK_REDO , '_Redo', '<control>Y',
            'Redo last actions', None),
            ('Cut',      gtk.STOCK_CUT , 'Cu_t', '<control>X',
            'Cut thing', None),
            ('Copy',      gtk.STOCK_COPY , '_Copy', '<control>C',
            'Copy thing', None),
            ('Paste',      gtk.STOCK_PASTE , '_Paste', '<control>V',
            'Paste thing', None),
            ('Preferences',      gtk.STOCK_PASTE , 'Preference_s', '<control><alt>P',
            'Edit preferences', None),

            ('ElementosMenu', None, '_Elements'),

            ('NewRange',   gtk.STOCK_NEW , 'New experimental data', '<ctrl>D',
             'Create a new set of experimental data', self._on_new_experimentalData),
            ('EditRange',      gtk.STOCK_EDIT , 'Edit experimental data', '<alt><shift>D',
            'Edit experimental data', self._on_edit_experimentalData),
            ('DeleteRange',      gtk.STOCK_DELETE, 'Delete experimental data', '<ctrl><shift>D',
            'Delete', self._on_delete_experimentalData),

            ('NewEquation',      gtk.STOCK_NEW , 'New equation', '<ctrl>E',
             'Create a new equation', self._on_new_equation),
            ('EditEquation',      gtk.STOCK_EDIT , 'Edit equation', '<alt><shift>E',
            'Edit thing', self._on_edit_equation),
            ('DeleteEquation',      gtk.STOCK_DELETE, 'Delete equation', '<ctrl><shift>E',
            'Delete', self._on_delete_equation),

            ('HelpMenu', None, '_Help'),
            ('Debug',    None, '_Debug', None, 'Toggle debug mode on|off',
             self._on_action_help),
            ('About',    None, '_About', None, 'About application',
             self._on_action_about),
            ]

        ag.add_actions(actions)

        ui.insert_action_group(ag, 0)
        ui.add_ui_from_string(self.get_ui_string())

        window.add_accel_group(ui.get_accel_group())

        return ui

    def update_graph(self):

        fig = self.get_fig()

        hayQueReplotear = self.get_setupView().get_hayQueReplotear()

        print 'fig = ',fig
        print 'hayQueReplotear =',hayQueReplotear

        if fig == None or hayQueReplotear:

            if fig == None:  # entonces hay que replotear.

                fig = Figure(figsize=(self.get_setupView().get_figureSizeH(), self.get_setupView().get_figureSizeV()), dpi=self.get_setupView().get_dpi())
                self.set_fig(fig)
                self.set_canvas(FigureCanvas(self.get_fig()))  # a gtk.DrawingArea

            #~ self.subp = self.fig.add_subplot(111)
            self.subp = self.fig.add_subplot(1,1,1)

            if self.get_setupView().get_logX() and self.get_setupView().get_logY():
                self.get_subp().loglog([1], [1e-6], 'k+')

            if not(self.get_setupView().get_logX()) and self.get_setupView().get_logY():
                self.get_subp().semilogy([0.],[1e-6],'k+')

            if self.get_setupView().get_logX() and not(self.get_setupView().get_logY()):
                self.get_subp().semilogx([1.],[0.],'k+')

            if not(self.get_setupView().get_logX()) and not(self.get_setupView().get_logY()):
                self.get_subp().plot([0.],[0.],'k+')


        self.get_subp().get_axes().grid(b=self.get_setupView().get_majorgridb(), which='major', color=self.get_setupView().get_majorgridbColor(), linestyle=self.get_setupView().get_majorgridlinestyle())
        self.get_subp().get_axes().grid(b=self.get_setupView().get_minorgridb(), which='minor', color=self.get_setupView().get_minorgridbColor(), linestyle=self.get_setupView().get_minorgridlinestyle())

        self.set_axes(self.subp.get_axes())
        self.subp.get_axes().grid(True)


        xaxisType = 'linear'
        if self.get_setupView().get_logX():
            xaxisType = 'log'
        self.subp.get_axes().set_xscale(xaxisType)
        yaxisType = 'linear'
        if self.get_setupView().get_logY():
            yaxisType = 'log'
        self.subp.get_axes().set_yscale(yaxisType)


        self.set_xlim0(self.get_setupView().get_xlim0())
        self.set_xlim1(self.get_setupView().get_xlim1())
        self.set_ylim0(self.get_setupView().get_ylim0())
        self.set_ylim1(self.get_setupView().get_ylim1())

        if (self.get_xlim0() != None) and (self.get_xlim1() != None):
            self.get_subp().get_axes().set_xlim((self.get_xlim0(),self.get_xlim1()))
            #~ print 'self.get_subp().get_axes().get_xlim()=',self.get_subp().get_axes().get_xlim()

        if (self.get_ylim0() != None) and (self.get_ylim1() != None):
            self.get_subp().get_axes().set_ylim((self.get_ylim0(),self.get_ylim1()))
            #~ print 'self.get_subp().get_axes().get_ylim()=',self.get_subp().get_axes().get_ylim()

        self.get_subp().axes.set_xlabel(str(self.get_setupView().get_xlabel()))

        self.get_subp().get_axes().set_ylabel(str(self.get_setupView().get_ylabel()))

        self.get_canvas().draw()
        #~ self.get_canvas().reset_shapes()
        self.get_canvas().show_all()

        self.get_gtkWindow().show()

        return None


    def setup(self, setupElement = None):
        if setupElement == None:
            setupElement = self.get_setupView()
        else:
            self.set_setupView(setupElement)

        return None


    def checkExistence(self, labelsTxt):

        repeated = True
        ok = True
        # input name and geometry values
        print "labelsTxt = ",labelsTxt
        valuesIn = ['']
        howwas = True

        while (repeated and ok):
            valuesOut = self.editText(labelsTxt, valuesIn)   # editText
            if valuesOut[1]:
                # check for repeated
                # lista de nombres de cosas existentes.
                listNoms = []
#~
                #~ for thing in things:
                    #~ listNoms.append(thing.get_name())

                if valuesOut[0][0] in listNoms:
                    repeated = True
                    # --- Repeated data dialog
                    current = str(valuesOut[0][0])
                    dialog = gtk.MessageDialog(self,
                        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                        current+" already exists. \n Please enter a new name.")
                    dialog.run()
                    dialog.destroy()
                    okStatus = False
                    # --- end of dialog.
                else:
                    repeated = False
                    nameIn = valuesOut[0]
            else:
                ok = False
                howwas = False
        if valuesOut[1]:
            return valuesOut, True
        else:
            return None, False


    def editText (self, labelsIn=None, valuesIn=None, dialogLabel='  ', okLabel=gtk.STOCK_OK, cancelLabel=gtk.STOCK_CANCEL):
        #~ print 'en editText,   labelsIn=',labelsIn, '  valuesIn=',valuesIn
        I=0

        valuesOut = np.copy(valuesIn)
        valuesNow = np.copy(valuesIn)
        wrongType = 1
        okStatus = True

        while wrongType>0 and okStatus:
            wrongType = 0

            dialog = gtk.Dialog(dialogLabel, self.get_gtkWindow(), 0,
                    (okLabel, gtk.RESPONSE_OK,
                    cancelLabel, gtk.RESPONSE_CANCEL))

            hbox = gtk.HBox(False, 4)
            hbox.set_border_width(4)
            dialog.vbox.pack_start(hbox, False, False, 0)

            stock = gtk.image_new_from_stock(
                    gtk.STOCK_DIALOG_QUESTION,
                    gtk.ICON_SIZE_DIALOG)
            hbox.pack_start(stock, False, False, 0)


            table = gtk.Table(len(labelsIn), 2)
            table.set_row_spacings(4)
            table.set_col_spacings(4)
            hbox.pack_start(table, True, True, 0)

            entries=[]
            labels=[]

            #~ print 'en editText:  len(labelsIn)=',len(labelsIn)

            for I in range(len(labelsIn)):

                #~ print '  I=',I

                # label definition for entry.
                objLabel = gtk.Label(labelsIn[I])
                labels.append(objLabel)
                table.attach(objLabel,0,1,I,I+1)

                # entry definition.
                objEntry = gtk.Entry()
                objEntry.set_text(np.str(valuesIn[I]))
                entries.append(objEntry)
                table.attach(objEntry,1,2,I,I+1)
                objLabel.set_mnemonic_widget(objEntry)


            dialog.show_all()
            response = dialog.run()
            salida=[]              # list.
            if response == gtk.RESPONSE_OK:
                #~ print 'Click en ok,   len([labelsIn])=', len([labelsIn])
                okStatus = True

                for I in range(len(np.asanyarray(labelsIn))):
                    texto = entries[I].get_text().strip()

                    #~ print
                    #~ print 'I=',I,'  texto=',texto
                    if type(valuesIn[I]) == type('text'):

                        allSpaces = ([item in ' ' for item in texto].count(True) == len(texto))

                        if allSpaces or (len(texto)==0):
                            wrongType = wrongType + 1

                        else:
                            salida.append(texto)# text variable, always a name.
                    else:
                        anyText = ([item in nums for item in texto].count(False)>0)
                        #~ print 'anyText=',anyText
                        if anyText:
                            wrongType = wrongType + 1
                        else:
                            salida.append(np.float(texto))

                #~ print 'wrongType=',wrongType, ' okStatus=',okStatus
                if wrongType == 0:
                    valuesOut = salida
                else:
                    valuesNow = ' '
                    # --- Repeated data dialog
                    dialog2 = gtk.MessageDialog(self,
                        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                        " Wrong type or null entry. \n Please reenter data")
                    dialog2.run()
                    dialog2.destroy()
                    # --- end of dialog.
            else:
                #~ print 'Click en cancel'
                okStatus = False
                valuesOut = np.copy(valuesIn)

            #~ print 'en editText,   valuesOut',valuesOut
            dialog.destroy()


        return (valuesOut,okStatus)



    def _on_uimanager__connect_proxy(self, uimgr, action, widget):
        tooltip = action.get_property('tooltip')
        if not tooltip:
            return

        if isinstance(widget, gtk.MenuItem):
            cid = widget.connect('select', self._on_menu_item__select, tooltip)
            cid2 = widget.connect('deselect', self._on_menu_item__deselect)
            widget.set_data('pygtk-app::proxy-signal-ids', (cid, cid2))
        elif isinstance(widget, gtk.ToolButton):
            cid = widget.child.connect('enter', self._on_tool_button__enter, tooltip)
            cid2 = widget.child.connect('leave', self._on_tool_button__leave)
            widget.set_data('pygtk-app::proxy-signal-ids', (cid, cid2))

    def _on_uimanager__disconnect_proxy(self, uimgr, action, widget):
        cids = widget.get_data('pygtk-app::proxy-signal-ids')
        if not cids:
            return

        if isinstance(widget, gtk.ToolButton):
            widget = widget.child

        for name, cid in cids:
            widget.disconnect(cid)
        return None


    def _on_menu_item__select(self, menuitem, tooltip):
        self.statusbar.push(self._menu_cix, tooltip)
        return None

    def _on_menu_item__deselect(self, menuitem):
        self.statusbar.pop(self._menu_cix)
        return None



    def _on_new_experimentalData(self, widget, parent=None, parentId=None):
        valuesOut, statusOut = self.checkExistence(["Ingrese Nombre de nuevo set de datos:"])
        if statusOut:
            #~ print 'valuesOut[0]=',valuesOut[0][0]
            nombre = valuesOut[0][0]

            #~ serie = self.get_parent().create_dataSeries(name = nombre)
            serie = self.get_parent().create_element(elementType="<class '__main__.DataSeries'>", name=nombre)


            if serie != None:    # o sea, not None.

                archivoDeEntrada = ArchivoDeEntrada().chooseFile()

                separadores = [',', ' ', '\t','  ',';']
                proximo = True
                I = 0

                while proximo and I<len(separadores):
                    try:
                        data = archivoDeEntrada.getData(separador = separadores[I])

                        x = data[:,0]
                        y = data[:,1]

                        serie.set_data([x,y])
                        serie.set_markersize(6)
                        serie.set_markeredgewidth(2)
                        serie.set_linestyle('none')
                        serie.set_filled('none')
                        serie.set_marker('o')

                        self.plot_dataSeries(serie)
                        proximo = False

                    except:
                        I += 1

                    if not(proximo): break

                if proximo:     # no hubo forma de meter los datos con estos separadores.
                    self.get_parent().del_element(serie)    # algo salió como el culo y hay que reventar el objeto recién creado.

                #~ print 'data=',data

        return None


    def _on_edit_experimentalData(self, widget):

        print 'Llamada a editar datos experimentales...'

        nombres = self._get_experimentalDataList()

        opcion = Choices(nombres.keys(),texto ="Editar serie ...", pos = 0).dialogo()

        if opcion in nombres.keys():
            self._edit_dataSeries(nombres[opcion])

        return None


    def _on_delete_experimentalData(self, widget):

        print 'Llamada a borrar datos experimentales...'

        nombres = self._get_experimentalDataList()

        opcion = Choices(nombres.keys(),texto ="Eliminar serie ...", pos = 0).dialogo()

        if opcion in nombres.keys():

            if Choices(["¿ Está seguro ?"]).dialogo() != "¿ Está seguro ?":
                return None

            dataSeries = nombres[opcion]
            self.delete_experimentalData(dataSeries)

        return None


    def _get_experimentalDataList(self):

        modelsList = self.get_parent().get_modelsList()
        nombresDeEcuaciones = []

        for elementId, element in modelsList.items():
            nombresDeEcuaciones.append(element.get_name())

        # Busco las series que no tengan ecuación asociada. Ésas son las series experimentales.
        nombres = dict()

        dataSeriesList = self.get_parent().get_dataSeries()

        for nombre, serie in dataSeriesList.items():
            if not(serie.get_name() in nombresDeEcuaciones):
                nombres[serie.get_name()] = serie   # lo agrega al diccionario de series experimentales.

        return nombres


    def delete_experimentalData(self, dataSeries):

        graphPropertiesEditor = dataSeries.get_graphPropertiesEditor()
        if graphPropertiesEditor != None: graphPropertiesEditor.destroy()

        artista = dataSeries.get_artista()

        print 'Reventando al artista: ', artista
        if artista != None:
            try:
                artista.remove()    # a ver si esto anda
                del artista
                self.get_canvas().draw()
            except:
                print '    ...intento de borrar artista ya borrado del gráfico.'

        # finalmente se elimina el elemento de la lista de ecuaciones y la serie de datos asociada.
        if dataSeries != None:         self.get_parent().del_element(dataSeries)

        #~ self.get_canvas().draw()
        return None


    def _on_new_equation(self, widget):
    
        elementTypeDictNames = self.get_parent().get_elementTypeDictNames()
        if len(elementTypeDictNames) == 0:
            self.messageDialog("No se encontró el directorio de ecuaciones.\n\nRevisar el archivo de configuración Uirlis.cfg.")
        else:
            opcion = Choices(elementTypeDictNames.keys(),texto ="Elija tipo de ecuación nueva ...", pos = 0).dialogo()
    
            if opcion in elementTypeDictNames.keys():
                
                valuesOut, statusOut = self.checkExistence(["Ingrese Nombre de nueva ecuación:"])
                if statusOut:
                    #~ print 'valuesOut[0]=',valuesOut[0][0]
                    nombre = valuesOut[0][0]
    
                    creators = self.get_parent().get_elementTypeDict()
    
                    print '--------= En _on_new_equation()      creators:'
                    for clave, valor in creators.items(): print clave,', tipo:',type(clave), ', valor:',valor,', tipo:',type(valor)
                    print
                    print '         tipo elegido:   type(elementTypeDictNames[opcion]):',elementTypeDictNames[opcion], ', valor tipo:',type(elementTypeDictNames[opcion])
                    print
    
                    #~ Creator = creators[elementTypeDictNames[opcion]]
    
                    newModel = self.get_parent().create_element(elementType = elementTypeDictNames[opcion], name = nombre)     # después esto va por parámetro de tipo de ecuación.
    
                    if newModel != None:    # o sea, not None.
    
                        self.create_equation(newModel)
                        (x,y) = newModel.eval(newModel.get_indepVar())
                        
                        
                        serie = self.get_parent().create_element(elementType="<class '__main__.DataSeries'>", name=newModel.get_name())
                        serie.set_data([x,y])
                        serie.set_markersize(6)
                        serie.set_markeredgewidth(1.2)
                        serie.set_marker(None)
                                                
                        self.plot_dataSeries(serie)
                        
                        newModel.set_debug(self.get_debug())
                        serie.set_debug(self.get_debug())
        return None


    def create_equation(self, modelo):
        self.create_propertiesEditor(modelo)

        frame = self.get_frameList()[modelo]

        notebook = self.get_notebook()
        frames = notebook.get_children()

        if frame in frames:

            pageNumber = frames.index(frame)

        self.get_notebook().set_current_page(pageNumber)

        return None


    def _equations_floating_menu(self, texto, confirm=True, modelo=None):

        if modelo == None:

            elementsList = self.get_parent().get_elementsList()
            ecuaciones = []

            for elementId in elementsList.keys():
                print 'elementsList[elementId]=', elementsList[elementId],'  nombre=',elementsList[elementId].get_name()
                try:
                    if elementsList[elementId].is_equation(): ecuaciones.append(elementsList[elementId])
                except:
                    pass

            nombres = dict()
            for ecuacion in ecuaciones:
                nombres[ecuacion.get_name()]=ecuacion

            opcion = Choices(nombres.keys(),texto=texto, pos = 0).dialogo()

            if opcion in nombres.keys():
                modelo = nombres[opcion]

        if confirm and modelo != None:
            if Choices(["¿ Está seguro ?"]).dialogo() != "¿ Está seguro ?":
                modelo = None

        return modelo


    def _on_delete_equation(self, widget):

        print 'Llamada a borrar ecuaciones...'
        modelo = self._equations_floating_menu("Eliminar ecuación...")
        if modelo != None:
            self.delete_equation(modelo)

        return None


    def delete_equation(self, modelo):      ## este método es llamado desde el controlador al hacer New o Retrieve.

       # primero se borra la serie del gráfico.
        artista = self.get_parent().findArtistByModel(modelo)
        dataSeries = self.get_parent().findDataSeriesByArtist(artista)

        # esto destruye al graphPropertiesEditor
        if dataSeries != None:
            gpEditor = dataSeries.get_graphPropertiesEditor()
            if gpEditor != None: gpEditor.destroy()

        print 'Reventando al artista: ', artista
        if artista != None:
            artista.remove()    # a ver si esto anda
            del artista
            self.get_canvas().draw()

        # luego se borra de la vista (menú)
        print 'Borrando la vista del modelo ',modelo, ', llamado: ',modelo.get_name()
        self.deleteFrame(modelo)


        # finalmente se elimina el elemento de la lista de ecuaciones y la serie de datos asociada.
        if dataSeries != None:  self.get_parent().del_element(dataSeries)
        if modelo != None:      self.get_parent().del_element(modelo)
        return None


    def _on_edit_equation(self, widget):        # llamada desde el menú de la barra.

        print 'Llamada a editar ecuaciones...'
        modelo = self._equations_floating_menu("Editar ecuación...", confirm=False)
        if modelo != None:
            pageNumber = self.findPageNumberFromModel(modelo)
            self.get_notebook().set_current_page(pageNumber)
        return None


    def create_propertiesEditor(self, newModel, parent=None, parentId=None):

        frame = gtk.Frame()

        framein = gtk.EventBox()

        framein.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        framein.connect("button_press_event", self._on_equation_mouseEvent)

        frame.add(framein)

        frameEq = gtk.Frame()
        framein.add(frameEq)

        frameEq.show()
        framein.show()
        frame.show()

        nombre = newModel.get_name()

        label = gtk.Label(nombre)

        self.get_notebook().append_page(frame, label)

        self.assignFrame(newModel, frame)     # asigna número de página del notebook a este nuevo modelo.

        propiedades = PropertiesEditor(model=newModel, dict_entryTypes=self.get_dictTypeWidget(), ventana=frameEq)
        propiedades.set_subp(self.get_subp())
        if parent == None:
            propiedades.set_parent(self)
        else:
            propiedades.set_parent(parent)
        propiedades.run([])

        return None


    def _on_equation_mouseEvent(self, widget, event):   # este método captura los eventos sobre los tabs en donde están las ecuaciones.

        modeloAEditar = None
        try:
            if event.button == 3:
                print 'Right button clicked on widget ',widget
                print '     frame (widget parent)=',widget.get_parent()
                frame = widget.get_parent()

                modeloAEditar = None
                frames = self.get_frameList()
                for model, frameEq in frames.items():
                    print 'model=',model.get_name(),'  frameEq=',frameEq

                    if frameEq == frame: modeloAEditar = model

                print 'modeloAEditar=',modeloAEditar

        except:
            pass

        if modeloAEditar != None:

            metodos = dict()
            # menu con las opciones de edición “Editar propiedades de la serie de datos”,“Renombrar”,“Borrar”
            metodos["Editar propiedades gráficas de la serie de datos"] = self.edit_graphic_properties
            metodos["Renombrar"] = self.rename_equation
            metodos["Borrar"] = self.delete_equation_from_mouse_action

            opcion = Choices(metodos.keys(),texto="Editar ecuación "+modeloAEditar.get_name(), pos = 0).dialogo()

            if opcion in metodos.keys():
                metodos[opcion](modeloAEditar)
        return True


    def edit_graphic_properties(self, model):
        print 'Llamada a edit_graphic_properties.'
        self._edit_dataSeries(self.get_parent().findDataSeriesByArtist(self.get_parent().findArtistByModel(model)))
        return None


    def rename_equation(self, model):
        print 'Llamada a rename_equation.'
        valuesOut, statusOut = self.checkExistence(["Ingrese Nombre de nueva ecuación:"])
        if statusOut:
            print "Nombre nuevo para la ecuación y la serie de datos:", valuesOut[0]

            oldName = model.get_name()


            #~ # renombrar al frame que contiene la ecuación.
            frames = self.get_frameList()

            frameAEditar = None
            print 'model=',oldName
            for key, frameEq in frames.items():
                print key.get_name(),'  frameEq=',frameEq
                if key.get_name() == oldName: frameAEditar = frameEq

            if frameAEditar != None:
                #~ label = gtk.Label(valuesOut[0][0])
                label = self.get_notebook().get_tab_label(frameAEditar)
                label.set_text(valuesOut[0][0])

                self.get_notebook().queue_draw_area(0,0,-1,-1)

                #~ print 'dir(frameAEditar)='
                #~ for item in dir(frameAEditar): print item

            # renombrar a la serie de datos.
            allDataSeries = self.get_parent().get_dataSeries()

            print 'allDataSeries=',allDataSeries

            if allDataSeries != None:
                for key, dataSeries in allDataSeries.items():
                    if oldName == dataSeries.get_name():
                        dataSeries.set_name(valuesOut[0][0])
                        artista = dataSeries.get_artista()
                        artista.set_label(valuesOut[0][0])


            # renombrar al modelo.
            print
            print '-----Nombre anterior:',oldName
            model.set_name(valuesOut[0][0])
            print '-----Nombre nuevo:',model.get_name()
            print



            #~
            #~ self.get_parent().updateModel(model)

        return None


    def delete_equation_from_mouse_action(self, modelo):
        modelo = self._equations_floating_menu(texto = "Eliminar ecuación...", confirm = True, modelo=modelo)
        if modelo != None: self.delete_equation(modelo)
        return None


    def __clearForLogScale(self, x0, y0):
        x1 = []
        y1 = []
        for I in range(len(x1)):
            if x0[I] > 0  and y0[I] > 0:
                x1.append(x0)
                y1.append(y0)
        return x0, y0


    def plot_dataSeries(self, serie, parent=None, parentId=None):

        if parent == None:
            serie.set_parent(self)
        else:
            serie.set_parent(parent)


        if parentId == None:
            serie.set_parentId(self.get_Id())
        else:
            serie.set_parentId(parentId)

        print '======================= plot_dataSeries'

        linewidth = serie.get_linewidth()

        (x,y)=serie.get_data()

        # Checkeo por existencia de ceros o negativos si algún eje es log.
        if self.get_setupView().get_logX() or self.get_setupView().get_logY():
            x,y = self.__clearForLogScale(x,y)

        # ploteo y eso.
        if self.get_setupView().get_logX() and self.get_setupView().get_logY():
            artistList = self.subp.loglog(x,y,linewidth=linewidth,picker=5)

        if not(self.get_setupView().get_logX()) and self.get_setupView().get_logY():
            artistList = self.subp.semilogy(x,y,linewidth=linewidth,picker=5)

        if self.get_setupView().get_logX() and not(self.get_setupView().get_logY()):
            artistList = self.subp.semilogx(x,y,linewidth=linewidth,picker=5)

        if not(self.get_setupView().get_logX()) and not(self.get_setupView().get_logY()):
            artistList = self.subp.plot(x,y,linewidth=linewidth,picker=5)


        artista = artistList[0]
        print '     artista =',artista

        serie.set_artista(artista)

        artista.set_label(serie.get_name())
        co = gtk.color_selection_palette_from_string(serie.get_colour())[0]

        color = (co.red_float,co.green_float,co.blue_float)
        artista.set_color(color)
        artista.set_markeredgecolor(color)
        artista.set_marker(serie.get_marker())
        artista.set_linestyle(serie.get_linestyle())
        artista.set_markersize(serie.get_markersize())
        artista.set_markeredgewidth(serie.get_markeredgewidth())
        artista.set_fillstyle(serie.get_filled())

        artista.set_visible(serie.get_visible())

        self.get_canvas().draw()


        return None


    def onclick(self, event):

        """Deal with click events"""
        button = ['left','middle','right']
        toolbar = plt.get_current_fig_manager().toolbar
        if toolbar.mode!='':
            print("You clicked on something, but toolbar is in mode {:s}.".format(toolbar.mode))
        else:
            print("You {0}-clicked coords ({1},{2}) (pix ({3},{4}))".format(button[event.button-1],\
                                                                                 event.xdata,\
                                                                                 event.ydata,\
                                                                                 event.x,\
                                                                                 event.y))
            #~ print 'event.xdata=',event.xdata, ',  event.ydata=',event.ydata

            if (event.xdata == None) and (event.ydata == None):  # picó en la zona fuera de las coordenadas del gráfico.
                print "Picó fuera del plot."
                self.get_setupView().run_dialog()

        print


    def onpick(self, event):

        artista = event.artist
        dataSeries = self.get_parent().findDataSeriesByArtist(artista)

        modelsList = self.get_parent().get_modelsList()

        dale = False

        for key, model in modelsList.items():
            if model.get_name() == dataSeries.get_name():
                modelo = model
                dale = True

        if dale:
            page = self.findPageNumberFromModel(modelo)
            self.get_notebook().set_current_page(page)

        if event.mouseevent.button == 3:
            self._edit_dataSeries(dataSeries, artista)

        if event.mouseevent.button == 1:
            pass
        return None


    def _edit_dataSeries(self, dataSeries, artista=None):
        if dataSeries.get_graphPropertiesEditor() == None:
            if artista == None:
                artista = dataSeries.get_artista()
            editor = GraphPropertiesEditor(dataSeries=dataSeries, artista=artista, title='Editar propiedades gráficas')
            dataSeries.set_graphPropertiesEditor(editor)
            editor.run()
        else:
            dataSeries.get_parent().get_parent().updateDataSeries(artista)
            dataSeries.get_graphPropertiesEditor().run()
        return None


    def assignFrame(self, model, frame):
        frameList = self.get_frameList()
        frameList[model] = frame

        print 'Asignando a modelo ',model.get_name(),' el frame ',frame,' en frameList.  frameList=', frameList

        self.set_lastPage(self.get_lastPage()+1)

        return None

    def findPageNumberFromModel(self, model):

        frameList = self.get_frameList()
        pageNumber = None
        frames = self.get_notebook().get_children()
        if frameList[model] in frames:
            pageNumber = frames.index(frameList[model])

        return pageNumber   # integer


    def deleteFrame(self, model):

        frameList = self.get_frameList()
        print 'frameList =', frameList

        #~ page =
        print 'En deleteFrame(), removiendo frame nro frameList[model]:',frameList[model]

        notebook = self.get_notebook()
        frames = notebook.get_children()
        if frameList[model] in frames:
            pageNumber = frames.index(frameList[model])
            notebook.remove_page(pageNumber)
            notebook.queue_draw_area(0,0,-1,-1)  # fuerza al refresco del notebook.

        del frameList[model]

        self.set_frameList(frameList)

        lastpage = self.get_lastPage()
        self.set_lastPage(lastpage-1)

        self.set_frameList(frameList)
        frameList = self.get_frameList()
        print 'frameList =', frameList
        print '    notebook.get_children():'
        for item in notebook.get_children(): print '    ',item

        return None


    def updateModel(self, modelo):
        print 'En clase View(), updateModel, modelo:',modelo.get_name()

        self.get_parent().updateModel(modelo)   # comando para el controller.
        return None


    def _on_action_new(self, action):
        elecciones = ['Descartar sesión actual']
        eleccion = Choices(elecciones).dialogo()

        if eleccion != "Cancel":
            self.new()

        return None


    def new(self):
        print ("New")
        #~ print 'dir(self.get_canvas())=',dir(self.get_canvas())
        self.get_parent().limpiarTodo()

        return None


    def persist(self, widget):
        print 'Persist... '
        print ("Save")

        self.filew = gtk.FileSelection("Save session to file")
        self.filew.ok_button.connect("clicked", self.get_parent().save_file_ok_sel, self.filew)

        # Connect the cancel_button to destroy the widget
        self.filew.cancel_button.connect("clicked", lambda w: self.filew.destroy())
        self.filew.show()

        return None


    def retrieve(self, widget):

        print 'Retrieve...'
        elecciones = ['Descartar sesión actual']
        eleccion = Choices(elecciones).dialogo()

        if eleccion != "Cancel":

            dialog = gtk.FileChooserDialog("Open..",
                                           None,
                                           gtk.FILE_CHOOSER_ACTION_OPEN,
                                           (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                            gtk.STOCK_OPEN, gtk.RESPONSE_OK))
            dialog.set_default_response(gtk.RESPONSE_OK)

            filter = gtk.FileFilter()
            filter.set_name("All files")
            filter.add_pattern("*")
            dialog.add_filter(filter)

            response = dialog.run()
            if response != gtk.RESPONSE_OK:

                print 'Closed, cancelled, escaped, or no files selected'
                dialog.destroy()
                return None


            print dialog.get_filename(), 'selected'
            filename = dialog.get_filename()
            dialog.destroy()

            # borra todos los elementos antes de cargar.
            self.get_parent().limpiarTodo()

            # acá va el algoritmo de limpiar todo.
            self.get_parent().retrieve(filename)

        return None


    def _on_action_help(self, action):
        self.help()
        return None

    def help(self):
        
        if self.get_debug():
            print ("Poniendo debug off a todos los objetos.")
            self.messageDialog("Debug to console set to OFF for every object.")
            self.set_debug(False)
        else:
            print ("Poniendo debug on a todos los objetos.")
            self.messageDialog("Debug to console set to ON for every object.")
            self.set_debug(True)
            
        elementsList = self.get_parent().get_elementsList()

        for clave, objeto in elementsList.items():
            
            print objeto.get_debug()
            objeto.set_debug(not(objeto.get_debug()))
            
        return None


    def _on_action_about(self, action):
        self.about()
        return None

    def about(self):
        print ("About")
        message = "\n                              Uirlis\n\n" 
        message +="   Graficador de ecuaciones y series de datos\n\n"
        message +="                     Copyleft (C) 2016"
        message +="\n\n Gustavo E. Carr Ph.D. - gecarr @ fi.mdp.edu.ar"
        message +="\n\n                       Licencia GPLv3"
        self.messageDialog(message)
        return None


    def _on_action_quit(self, action):
        self.quit()
        return None

    def _on_delete_event(self, window, event):
        print ("Ventana de la aplicación destruida por usuario. Cerrando...")
        self.quit()
        return gtk.TRUE

    def quit(self):
        if Choices(["Quit"]).dialogo() == "Quit":
            print ("Quit")
            gtk.main_quit()
        return None


    def messageDialog(self, message):
        dialog = gtk.MessageDialog(self.get_gtkWindow(),
                        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                        message)
        dialog.run()
        dialog.destroy()
        return True
        
# -------------------------
#
#
#
#
# -------------------------
class BoolEntry(gtk.HBox):

    def __init__(self, value=""):

        gtk.HBox.__init__(self)

        try:
            self.button = gtk.CheckButton()
        except:
            print 'Saltó en:   self.button = gtk.Checkbutton()'

        try:
            self.pack_start(self.button, True, True, 2)
        except:
            print 'Saltó en:   self.pack_start(self.button)'

        try:
            self.set_activates_default(True)
        except:
            pass

        self.callback = None

        return None

    def set_value(self, value):
        self.button.set_active(value)
        return None

    def get_value(self):
        return self.button.get_active()


    def set_callback(self, method):
        self.callback = method
        return None


    def get_callback(self):
        return self.callback


    def modified(self, widget, entry, dummy=None):
        callback = self.get_callback()
        if callback != None:
            callback()
        return None

# -------------------------
#
#
#
#
# -------------------------
class TextEntry(gtk.Entry):

    def __init__(self, value=""):

        gtk.Entry.__init__(self)

        self.set_text(str(value))
        self.connect("activate",self.modified, self)
        self.set_activates_default(True)
        #~ self.connect("focus-out-event",self.modified, self)
        #~ self.connect("insert-text",self.modified, self)
        self.callback = None

        return None

    def set_value(self, value):
        self.set_text(str(value))
        return None

    def get_value(self):
        return self.get_text().strip()


    def set_callback(self, method):
        self.callback = method
        return None


    def get_callback(self):
        return self.callback


    def modified(self, widget, entry, dummy=None):
        callback = self.get_callback()
        if callback != None:
            callback()
        return None

# -------------------------
#
#
#
#
# -------------------------
class NumericEntry(gtk.Entry):

    def __init__(self, value=0.0):

        gtk.Entry.__init__(self)

        self.set_text(np.str(value))

        self.connect("activate",self.modifCoef, self)
        self.connect("paste-clipboard",self.modifCoef, self)

        self.callback = None
        #~ self.set_digits(digits)
        #~ self.adj.set_value(value)
        self.set_value(value)

        return None


    def __validate(self, valor):

        try:
            float(valor)
            return True
        except:
            return False



    def set_callback(self, method):
        self.callback = method
        return None

    def get_callback(self):
        return self.callback


    def set_value(self, value):
        #~ self.adj.set_value(value)
        self.value = float(value)
        self.set_text(np.str(value))
        #~ self.set_increments(value*0.01, value*0.005)
        return None

    def get_value(self):
        return self.value


    #~ def modifCoef(self,widget,spinner, I):   # formato spin
    def modifCoef(self,widget,entry):
        valor = widget.get_text()
        if self.__validate(valor):
            self.set_value(valor)
            print 'Valor ',valor,' es float.'
        else:
            print 'Valor ',valor,' no es float.'
            return None

        callback = self.get_callback()
        if callback != None:
            callback()
        return None

    def set_digits(self, digits):
        return None

# -------------------------
# -------------------------
#
#
#
#
# -------------------------
class RangeEntry(gtk.Frame):

    def __init__(self, value=[0.0, 1.0, 0.1], callback=None):

        gtk.Frame.__init__(self)

        self.callback = callback

        self.p = [1.0E-6, 1.0E-3, 1.E-6]

        self.set_name("Independent variable")

        v2box = gtk.VBox(False, 0)
        v2box.set_border_width(5)
        self.add(v2box)
        # -- Spin buttons.
        hbox = gtk.VBox(False, 0)
        v2box.pack_start(hbox, False, True, 5)
        
        # Label.
        label = gtk.Label("Independent variable")


        # spin button 'a'
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

        label = gtk.Label("Min value=")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)

        adj1 = gtk.Adjustment(0.0, -10000.0, 10000.0, 0.001, 10.0, 0.0)
        self.spinner1 = gtk.SpinButton(adj1, 0.01*self.p[0], 10)
        self.spinner1.set_wrap(True)
        self.spinner1.set_value(self.p[0])

        vbox2.pack_start(self.spinner1, False, True, 0)

        # spin button 'b'
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

        label = gtk.Label("Max value=")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)

        adj2 = gtk.Adjustment(0.0, -10000.0, 10000.0, 0.001, 100.0, 0)
        self.spinner2 = gtk.SpinButton(adj2, 0.01*self.p[1], 10)
        self.spinner2.set_wrap(True)
        self.spinner2.set_value(self.p[1])

        vbox2.pack_start(self.spinner2, False, True, 0)


        # spin button 'c'
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

        label = gtk.Label("Step=")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)

        adj3 = gtk.Adjustment(0.0, -10000.0, 10000.0, 0.001, 100.0, 0)

        self.spinner3 = gtk.SpinButton(adj3, 0.01*self.p[2], 10)
        self.spinner3.set_wrap(True)
        self.spinner3.set_value(self.p[2])
        vbox2.pack_start(self.spinner3, False, True, 0)

        # seteo de valores iniciales.
        self.p[0] = value[0]
        self.p[1] = value[-1]
        step = int((self.p[1]-self.p[0]))/len(value)
        if step == 0.0: step = self.p[0]*0.1
        self.p[2] = step

        self.value = value

        self.spinner1.set_value(self.p[0])
        self.spinner2.set_value(self.p[1])
        self.spinner3.set_value(self.p[2])

        # conección de los callbacks recién ahora.
        adj1.connect("value_changed", self.modifCoef, self.spinner1, 1)
        adj2.connect("value_changed", self.modifCoef, self.spinner2, 2)
        adj3.connect("value_changed", self.modifCoef, self.spinner3, 3)

        return None


    def set_callback(self, method):
        self.callback = method
        return None

    def get_callback(self):
        return self.callback


    def set_value(self, value):
        self.value = value  # setea a la lista.
        return None

    def get_value(self):
        return self.value


    def modifCoef(self,widget,spinner,I):
        self.p[I-1] = widget.get_value()
        print 'widget.get_value()=',widget.get_value()
        print 'spinner=',spinner

        dale = True
        if self.p[0]>self.p[1]:
            dale = False
        if self.p[2]>(np.abs(self.p[1]-self.p[0])):
            dale = False
        if dale:
            hasta = self.p[2]+self.p[1]
            aes = np.mgrid[self.p[0]:hasta:self.p[2]]
            print ' Valores para rango=', self.p[0], self.p[1], self.p[2], ', min, max aes=',aes[0], aes[-1]
            self.set_value(aes)

        callback = self.get_callback()
        if callback != None:
            callback()

        return

# -------------------------
#
#
#
#
# -------------------------
class ColourButton(gtk.ColorButton):
    def __init__(self, colour='#F0F0F0', callback=None):
        gtk.ColorButton.__init__(self)

        self.set_color(gtk.color_selection_palette_from_string(colour)[0])

        self.callback = callback

        self.set_use_alpha(False)
        self.set_title('Select a Color')
        self.set_alpha(65535)
        self.connect('color-set', self.colour_set_cb)        #~ hbox.pack_start(colorbutton)

        self.colour = colour

        return None


    def set_callback(self, method):
        self.callback = method
        return None

    def get_callback(self):
        return self.callback


    def colour_set_cb(self, colourbutton):

        self.colour = self.get_color()

        return

    def set_value(self, colour):
        self.colour = colour
        #~ self.colourbutton.set_color(colour)
        self.set_color(gtk.color_selection_palette_from_string(colour)[0])

    def get_value(self):

        return self.get_color().to_string()

# -------------------------
#
#
#
#
# -------------------------
#~ class CellRendererSpinWindow(gtk.ScrolledWindow):
class CellRendererSpinWindow(gtk.VBox):

    def __init__(self, datos=None, callback=None):

        gtk.VBox.__init__(self)

        self.sw = gtk.ScrolledWindow()

        self.callback = callback

        self.pack_start(self.sw)

        self.rows = 0
        self.x = []
        self.y = []
        self.liststore = gtk.ListStore(float, float)

        self.datos = datos

        self.set_size_request(100,150)

        self.treeview = gtk.TreeView(model=self.liststore)

        renderer_spin1 = gtk.CellRendererText()
        renderer_spin1.connect("edited", self.on_amount_editedX)

        renderer_spin1.set_property("editable", True)

        column_spin1 = gtk.TreeViewColumn("X", renderer_spin1, text=0)
        column_spin1.set_property("expand", True)
        renderer_spin1.set_property("text", "{0}".format(0.000000000000001))

        column_spin1.set_cell_data_func(renderer_spin1, \
                lambda col, cell, model, iter: cell.set_property("text",
                "{0}".format(self.truncate(model.get(iter, 0)[0]))))

        self.treeview.append_column(column_spin1)

        renderer_spin2 = gtk.CellRendererText()
        renderer_spin2.connect("edited", self.on_amount_editedY)
        renderer_spin2.set_property("editable", True)

        column_spin2 = gtk.TreeViewColumn("Y", renderer_spin2, text=1)
        column_spin2.set_property("expand", True)
        column_spin2.set_cell_data_func(renderer_spin2, \
                lambda col, cell, model, iter: cell.set_property("text",
                "{0}".format(self.truncate(model.get(iter, 1)[0]))))

        self.treeview.append_column(column_spin2)

        self.treeview.show()

        self.sw.add_with_viewport(self.treeview)

        self.set_child_visible(True)
        self.show()

        if datos != None:
            self.set_value(datos)

        return None

    def truncate(self, number):
        """
        Rounds and truncates a number to one decimal place. Used for all
        float numbers in the data-view. The numbers are saved with full float
        precision.
        """
        #~ number = round(number, 1)
        return number

    def set_value(self, datos):
        x = datos[0]
        y = datos[1]

        self.rows = len(x)

        for I in range(0,self.rows):
            self.liststore.append(row=(x[I],y[I]))
        return None



    def set_callback(self, method):
        self.callback = method
        return None

    def get_callback(self):
        return self.callback


    def on_amount_editedX(self, widget, path, value):
        self.on_amount_edited(widget, path, value, 0)
        return None


    def get_rows(self):
        return self.rows


    def on_amount_editedY(self, widget, path, value):
        self.on_amount_edited(widget, path, value, 1)
        return None


    def on_amount_edited(self, widget, path, value, col):

        iter = self.liststore.get_iter(path)
        #~ print 'iter=',iter

        self.liststore.set_value(iter, col, float(value))

        data = self.get_value()
        #~ print data
        return None

    def on_row_deleted(self, button):

        return None


        #~ print 'dir(button)=',dir(button)

        if Choices(["Delete"]).dialogo() == "Delete":


            selection = self.treeview.get_selection()
            # get_selected_rows() returns a tuple
            # The first element is a ListStore
            # The second element is a list of tree paths
            # of all selected rows
            model, paths = selection.get_selected_rows()

            print 'paths=',paths

            # Get the TreeIter instance for each path
            for path in paths:
                print '     path=',path
                iter = model.get_iter(path)
                # Remove the ListStore row referenced by iter
                self.model.remove(iter)

        return None


    def get_value(self):

        rows = self.get_rows()
        x = []
        y = []
        for I in range(0,rows):
            iter = self.liststore.get_iter(I)
            x.append(self.liststore.get_value(iter, 0))
            y.append(self.liststore.get_value(iter, 1))
            #~ print 'Row:',I,'  x=',self.liststore.get_value(iter, 0),'  y=',self.liststore.get_value(iter, 1)
        data = [x,y]
        return data

    def get_text(self):
        return 'Texto'
# -------------------------
#
#
#
#
# -------------------------
class GraphPropertiesEditor():

    def __init__(self, dataSeries=None, artista=None, title='Editar propiedades'):

        #~ gtk.Window.__init__(self)

        self.dict_entryTypes = dict(name = TextEntry,
                                marker = TextEntry,
                                markersize = NumericEntry,
                                markeredgewidth = NumericEntry,
                                linestyle = TextEntry,
                                data = CellRendererSpinWindow,
                                colour = ColourButton,
                                visible = BoolEntry,
                                linewidth = TextEntry,
                                filled = TextEntry)

        self.dataSeries  = dataSeries
        self.artista = artista
        self.titulo = title
        self.ventana = None
        self.entries = []

        return None


    def run(self, applyLabel=gtk.STOCK_APPLY, okLabel=gtk.STOCK_OK, cancelLabel=gtk.STOCK_CANCEL):

        print 'en propertiesEditor.run(), artista=',self.get_artista()
        ventana = self.get_ventana()
        if ventana != None:
            print 'ventana=',ventana
            ventana.show()
            return None

        dataSeries = self.get_dataSeries()

        #~ valuesIn = []
        getters = dataSeries.get_dict_getters()
        UIgetters = self.get_dict_entryTypes()

        orden = dataSeries.get_dict_UIkeys()
        labelsIn = dataSeries.get_UILabels()

        self.ventana = gtk.Window() #, None, 0,

        self.ventana.set_default_size(200, 200)

        #~ self.ventana.set_title(self.get_titulo())
        self.ventana.set_title("Edit "+self.get_dataSeries().get_name())
        self.ventana.connect("destroy", self.on_cancel)
        self.ventana.connect("delete-event", self.on_cancel)

        hbox = gtk.HBox(False, 4)
        hbox.set_border_width(4)
        self.ventana.add(hbox)


        table = gtk.Table(len(labelsIn)+1, 2)
        table.set_row_spacings(4)
        table.set_col_spacings(3)
        hbox.pack_start(table, True, True, 0)

        entries=[]
        labels=[]

        for I in range(len(orden)):

            print

            # label definition for entry.
            objLabel = gtk.Label(labelsIn[I])
            labels.append(objLabel)
            table.attach(objLabel,0,1,I,I+1)

            try:
                objEntry = UIgetters[orden[I]]()
                objEntry.set_value(getters[orden[I]]())     # acá asigna los valores a los objetos de entrada.
                objEntry.set_callback(self.on_modifCoef)
            except:
                print "Object entry creation failure for key:", orden[I]

            entries.append(objEntry)
            table.attach(objEntry,1,3,I,I+1)
            objLabel.set_mnemonic_widget(objEntry)

        self.set_entries(entries)

        applyButton = gtk.Button('Aplicar')
        applyButton.connect("clicked", self.on_apply)

        okButton = gtk.Button('OK')
        okButton.connect("clicked", self.on_ok)

        cancelButton = gtk.Button('Cancelar')
        cancelButton.connect("clicked", self.on_cancel)

        table.attach(applyButton,0,1,I+1,I+2)
        table.attach(okButton,1,2,I+1,I+2)
        table.attach(cancelButton,2,3,I+1,I+2)
        hbox.show_all()
        
        self.ventana.show_all()
        
        return None

    # --------------------- Dictionaries getters.
    def get_dict_entryTypes(self):
        return self.dict_entryTypes

    # --------------------- Setters y getters
    def set_dataSeries(self, dataSeries):
        self.dataSeries = dataSeries
        return None

    def get_dataSeries(self):
        return self.dataSeries


    def set_artista(self, artista):
        self.artista = artista
        return None

    def get_artista(self):
        return self.artista


    def set_titulo(self, titulo):
        self.titulo = titulo
        return None

    def get_titulo(self):
        return self.titulo


    def set_ventana(self, ventana):
        self.ventana = ventana
        return None

    def get_ventana(self):
        return self.ventana


    def set_entries(self, entries):
        self.entries = entries
        return None

    def get_entries(self):
        return self.entries


    # --------------------- callbacks
    def on_ok(self, event):
        print 'En propertiesEditor.on_ok(),  artista=',self.get_artista()

        #~ valuesOut = salida
        self._setValuesToArtist()

        #~ self.blanquearEditor(event)
        self.destroy(event)
        return None


    def on_modifCoef(self):
        self.on_apply(None)
        return None


    def on_apply(self, event):
        print 'apply'

        #! Chequear cómo se articula esto que traje de la otra clase PropertiesEditor en esta.
        self._setValuesToArtist()

        return None


    def on_cancel(self, event):
        print 'Cancel'
        self.destroy(event)

        return None


    def blanquearEditor(self, event):

        self.get_ventana().destroy()
        return None


    def destroy(self, event=None):

        self.get_dataSeries().set_graphPropertiesEditor(None)
        self.get_ventana().destroy()

        return None


    def _setValuesToArtist(self):

        print 'En propertiesEditor._setValuesToArtist(),  artista=',self.get_artista()
        dataSeries = self.get_dataSeries()
        setters = dataSeries.get_dict_setters()
        getters = dataSeries.get_dict_getters()

        orden = dataSeries.get_dict_UIkeys()
        labelsIn = dataSeries.get_UILabels()

        entries = self.get_entries()

        for I in range(len(orden)):
            # acá le pide a cada entry los datos y se los pone al objeto con sus setters.
            setters[orden[I]](entries[I].get_value())

        return None



# ------------------------- fin clase GraphPropertiesEditor
#
#
#
#
# -------------------------
# -------------------------class DataSeries(Element):
class DataSeries(object):

    #~ def __init__(self, name='', data=[[1.],[1.]], marker=None, linestyle='-', linewidth=2.0, colour='#000000', eq=None, artista = None, parent=None, Id=None):
    def __init__(self, name='', data=[[1.],[1.]], marker=None, markersize=6, markeredgewidth=1, linestyle='-', linewidth=2.0, colour='#000000', eq=None, visible = True, artista = None, **kwargs):


        # ------------------- Diccionarios.
        self.dict_setters = dict()
        self.dict_setters.update(dict(name = self.set_name,
                data = self.set_data,
                marker = self.set_marker,
                markersize = self.set_markersize,
                markeredgewidth = self.set_markeredgewidth,
                filled = self.set_filled,
                linestyle = self.set_linestyle,
                linewidth = self.set_linewidth,
                colour = self.set_colour,
                visible = self.set_visible,
                parentId = self.set_parentId,
                type = self.set_type))

        self.dict_getters = dict()
        self.dict_getters.update(dict(name = self.get_name,
                data = self.get_data,
                marker = self.get_marker,
                markersize = self.get_markersize,
                markeredgewidth = self.get_markeredgewidth,
                filled = self.get_filled,
                linestyle = self.get_linestyle,
                linewidth = self.get_linewidth,
                colour = self.get_colour,
                visible = self.get_visible,
                parentId = self.get_parentId,
                type = self.get_type))


        setters = self.get_dict_setters()
        for key in setters.keys():
            if key in kwargs:   setters[key](kwargs[key])


        self.dict_UIkeys = ['visible','data','marker','markersize','markeredgewidth','linestyle','linewidth','colour','filled']
        self.dict_UIlabels = dict(name = 'Nombre',
                                data = 'Datos',
                                marker = 'Marcador',
                                markersize = 'Tamaño del marcador',
                                markeredgewidth = 'Ancho de línea del marcador',
                                linestyle = 'Tipo de linea',
                                linewidth = 'Ancho de línea de la serie',
                                colour = 'Color',
                                visible = 'Visible',
                                filled  = 'Relleno [none,top,bottom,left,right,full]')#,
                                #~ eq = 'Ecuacion')

        self.Id = None

        self._markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_', ' ']
        self._linestyles = ['-' , '--' , '-.' , ':', 'None', '']

        self.artista = None

        if "artista" in kwargs:
            self.artista = kwargs["artista"]

        self.parentId = None

        self.name = name
        self.data = data
        self.cr = CellRendererSpinWindow(data)

        self.linestyle = linestyle
        self.marker = marker
        self.markersize = markersize
        self.markeredgewidth = markeredgewidth
        self.filled = 'full'

        self.linewidth = linewidth
        self.colour = colour #gtk.gdk.color_parse(colour)
        self.visible = visible
        self.eq = eq
        self.graphPropertiesEditor = None
        #~ self.parent = parent

        # para cancel
        self._oldName = None
        self._oldLinewidth = None
        self._oldColour = None
        self._oldRelleno = None

        self.debug = False

        return None

    # --------------------------------------------- Setters and getters

    def get_dict_getters (self) :
        return self.dict_getters


    def get_dict_setters (self) :
        return self.dict_setters


    #~ def get_dict_UIgetters(self):
        #~ return self.dict_UIgetters


    def get_dict_UIkeys(self):
        return self.dict_UIkeys

    def get_dict_UIlabels(self):
        return self.dict_UIlabels


    # ----- setters and getters
    def set_Id(self, Id):           # este método se utiliza al deshidratar y rehidratar los objetos.
        self.Id = Id
        return None

    def get_Id(self):               # este método se utiliza al deshidratar y rehidratar los objetos.
        return self.Id


    def set_name(self, name):
        self.name = name
        return None

    def get_name(self):
        return self.name


    def set_type(self, type):
        # no se setea, es un método dummy
        return None

    def get_type(self):                 # este método se utiliza al deshidratar los objetos y sirve como clave para rehidratarlos.
        return str(type(self)).strip()


    def set_artista(self, artista):
        self.artista = artista
        return None

    def get_artista(self):
        return self.artista


    def set_data(self, data):
        self.data = data
        artista = self.get_artista()
        if artista != None:
            artista.set_xdata(data[0])
            artista.set_ydata(data[1])
            self.get_parent().get_canvas().draw()

        return None

    def get_data(self):
        return self.data


    def set_linestyle(self, linestyle):
        if not(linestyle in self._get__linestyles()):
            linestyle = ''
            print 'linestyle es un string vacío'

        self.linestyle = linestyle
        artista = self.get_artista()
        if artista != None:

            artista.set_linestyle(linestyle)
            self.get_parent().get_canvas().draw()

        #~ print 'en DataSeries.set_linestyle(),   linestyle es:', self.linestyle
        return None

    def get_linestyle(self):
        return self.linestyle


    def set_marker(self, marker):

        if not(marker in self._get__markers()):
            marker = None

        self.marker = marker
        artista = self.get_artista()
        if artista != None:
            artista.set_marker(marker)
            self.get_parent().get_canvas().draw()

        #~ print 'en DataSeries.set_marker(),   marker es:', self.marker
        return None

    def get_marker(self):
        return self.marker


    def set_markersize(self, markersize):

        try:
            isfloat = str(type(float(markersize))).strip() == "type<'float'>"
            if markersize > 0.0:
                self.markersize = markersize
                artista = self.get_artista()
                if artista != None:
                    artista.set_markersize(float(markersize))
                    self.get_parent().get_canvas().draw()
        except:
            pass

        return None

    def get_markersize(self):
        if self.markersize == None:
            return 6.0
        return self.markersize


    def set_markeredgewidth(self, markeredgewidth):

        if str(type(markeredgewidth)).strip() == "type<'float'>":
            if markeredgewidth > 0.0:
                self.markeredgewidth = markeredgewidth
                artista = self.get_artista()
                if artista != None:
                    artista.set_markeredgewidth(float(markeredgewidth))
                    self.get_parent().get_canvas().draw()

        return None

    def get_markeredgewidth(self):
        if self.markeredgewidth == None:
            return 1.0
        return self.markeredgewidth


    def set_linewidth(self, linewidth):
        #~ print 'dentro de dataSeries.set_linewidth(), seteando a linewidth=',linewidth
        self.linewidth = linewidth

        artista = self.get_artista()
        print 'tengo artista?   artista=',artista
        if artista != None:
            print 'setting linewidth'
            artista.set_linewidth(linewidth)
            self.get_parent().get_canvas().draw()
            #~ plt.show()
        return None

    def get_linewidth(self):
        return self.linewidth


    def set_colour(self, colour):
        self.colour = colour
        artista = self.get_artista()
        if artista != None:
            #~ print 'setting colour'
            co = gtk.color_selection_palette_from_string(self.get_colour())[0]
            color = (co.red_float,co.green_float,co.blue_float)
            artista.set_color(color)
            artista.set_markeredgecolor(color)

            artista.set_fillstyle(self.get_filled())
            #~ artista.draw()
            self.get_parent().get_canvas().draw()
            #~ plt.show()
        return None

    def get_colour(self):
        return self.colour


    def set_filled(self, filled):
        if (filled in ['none','top','bottom','right','left','full']):
            self.filled = filled
            artista = self.get_artista()
            if artista != None:
                artista.set_fillstyle(filled)
                self.get_parent().get_canvas().draw()
        return None

    def get_filled(self):
        return self.filled


    def set_visible(self, visible):
        self.visible = visible
        return None

    def get_visible(self):
        return self.visible


    def set_eq(self, eq):
        self.eq = eq
        return None

    def get_eq(self):
        return self.eq


    def set_graphPropertiesEditor(self, graphPropertiesEditor):
        self.graphPropertiesEditor = graphPropertiesEditor
        return None

    def get_graphPropertiesEditor(self):
        return self.graphPropertiesEditor


    def set_parent(self, parent):
        self.parent = parent
        return None

    def get_parent(self):
        return self.parent


    def set_parentId(self, parentId):
        self.parentId = parentId
        return None

    def get_parentId(self):
        return self.parentId


    def set_debug(self, debug):
        self.debug = debug
        return None

    def get_debug(self):
        return self.debug


    def is_equation(self):
        return False


    def _get__markers(self):
        return self._markers

    def _get__linestyles(self):
        return self._linestyles


    def get_x(self):
        data = self.get_data()
        return data[0]


    def get_y(self):
        data = self.get_data()
        return data[1]


    def get_UILabels(self):
        orden = self.get_dict_UIkeys()
        labelsTxt = []
        labels = self.get_dict_UIlabels()
        for item in orden:
             labelsTxt.append(labels[item])
        return labelsTxt


    # --------------------------------------------- Methodds
    def updateGraphPropertiesEditor(self):

        graphPropertiesEditor = self.get_graphPropertiesEditor()

        if graphPropertiesEditor != None:
            graphPropertiesEditor.blanquearEditor(None)
            self.set_graphPropertiesEditor(None)
            editor = GraphPropertiesEditor(dataSeries=self, artista=self.get_artista(), title='Editar propiedades gráficas')
            self.set_graphPropertiesEditor(editor)
            editor.run()
        #~ else:
            #~ graphPropertiesEditor.run()
        return None


    def is_equation(self):  # esto es para que plotee las dataSeries y no intente plotear las ecuaciones.
        return False


    def get_data_as_dict(self):

        self.dic = dict()
        getters = self.get_dict_getters()

        for clave in getters.keys():       # devuelve las claves o valores de los atributos en una lista.

            attrib = getters[clave]()       # devuelve el valor (u objeto) del getter.

            print '   En elemento:',self.get_name(),'.   atributo:',attrib, 'tipo :',type(attrib)

            if type(attrib) == type([1,2]):     #~ print 'es lista'
                print '                     .... el atributo es lista. Iterando elementos...'
                lista = []
                for item in attrib:

                    print '             en clase base Element, item de attrib:',item
                    try:
                        print '                                             intentando pedir data_as_dict del objeto.'
                        obj = item.get_data_as_dict()
                        lista.append(obj)

                    except:
                        print '                                             no dio data as dict, haciendo append del objeto.'
                        lista.append(item)

                self.dic[clave] = lista

            else:
                print '                     .... el atributo no es lista. Pidiendo data_as_dict'
                try:
                    obj = attrib.get_data_as_dict()
                    self.dic[clave] = obj
                    print '              self.dic[clave] = obj:  self.dic[',clave,']=',obj

                except:
                    self.dic[clave] = attrib

        return self.dic

# ------------------------- fin clase DataSeries.
#
#
#
#
#~ ------------------------------------------------  class PropertiesEditor:
class PropertiesEditor():

    def __init__(self, model=None, dict_entryTypes=dict(), ventana = None, subp = None):


        #~ gtk.Window.__init__(self)

        self.dict_entryTypes = dict()
        self.dict_entryTypes[str(type("aa"))] = TextEntry
        self.dict_entryTypes[str(type(1.0))]= NumericEntry
        self.dict_entryTypes[str(type([1,2]))] = RangeEntry
        self.dict_entryTypes["<type 'numpy.ndarray'>"] = RangeEntry

        self.model  = model
        #~ self.artista = artista
        self.ventana = ventana      # la ventana es la del diálogo de propiedades.
        self.parent = None  # es la vista.
        #~ self.subp = subp
        self.entries = []

        return None


    def run(self, applyLabel=gtk.STOCK_APPLY):

        ventana = self.get_ventana()

        model = self.get_model()

        #~ valuesIn = []
        getters = model.get_dict_getters()
        UIgetters = self.get_dict_entryTypes()

        orden = model.get_dict_UIkeys()
        labelsIn = model.get_UILabels()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.ventana.add(sw)

        hbox = gtk.HBox()

        sw.add_with_viewport(hbox)

        hbox.set_border_width(4)

        table = gtk.Table(len(labelsIn)+2, 2)

        table.set_row_spacings(4)
        table.set_col_spacings(3)

        hbox.pack_start(table, True, True, 0)

        entries=[]
        labels=[]

        print

        tipoDeModelo = "Tipo de modelo: "+model.get_model_name()
        objLabel = gtk.Label(tipoDeModelo)
        table.attach(objLabel,0,2,0,1)


        for I in range( len(orden)):


            # label definition for entry.
            objLabel = gtk.Label(labelsIn[I])
            labels.append(objLabel)
            table.attach(objLabel,0,1,I+1,I+2)

            try:
                objEntry = UIgetters[str(type(getters[orden[I]]() ))](value=getters[orden[I]]())
            except:
                print "Object entry creation failed in key: ",orden[I]

            objEntry.set_callback(self.on_modifCoef)    # primero va el callback porque salta el callback de modifcoef al asignarle valor con set_value.
            entries.append(objEntry)
            table.attach(objEntry,1,3,I+1,I+2)
            objLabel.set_mnemonic_widget(objEntry)

        self.set_entries(entries)

        applyButton = gtk.Button('Aplicar')
        applyButton.connect("clicked", self.on_apply)


        table.attach(applyButton,0,1,I+2,I+3)

        hbox.show_all()
        sw.show()

        self.ventana.show_all()

        return None

    # --------------------- Dictionaries getters.
    def get_dict_entryTypes(self):
        return self.dict_entryTypes

    # --------------------- Setters y getters
    def set_model(self, model):
        self.model = model
        return None

    def get_model(self):
        return self.model


    def set_parent(self, parent):
        self.parent = parent
        return None

    def get_parent(self):
        return self.parent


    def set_artista(self, artista):
        self.artista = artista
        return None

    def get_artista(self):
        return self.artista


    def set_ventana(self, ventana):
        self.ventana = ventana
        return None

    def get_ventana(self):
        return self.ventana


    def set_subp(self, subp):
        self.subp = subp
        return None

    def get_subp(self):
        return self.subp


    def set_entries(self, entries):
        self.entries = entries
        return None

    def get_entries(self):
        return self.entries


    # --------------------- callbacks
    def on_modifCoef(self):
        self.on_apply(None)
        return None


    def on_apply(self, event):
        print 'apply'

        modelo = self.get_model()

        setters = modelo.get_dict_setters()
        UIgetters = self.get_dict_entryTypes()

        entries = self.get_entries()

        orden = modelo.get_dict_UIkeys()

        for I in range(len(orden)):
            setters[orden[I]](entries[I].get_value())           # esto pone los valores de la gui en el modelo.

        self.get_parent().updateModel(modelo)

        return None


    def on_cancel(self, event, dummy):
        print 'Cancel.   event=',event,'   dummy=',dummy
        self.blanquearEditor(event)

        return None

    def blanquearEditor(self, event):

        print 'event=',event#,',   data=',data


        return None

# ------------------------- fin clase PropertiesEditor.
#
#
#
#
#~ ------------------------------------------------  class Choices:
class Choices:

    def __init__ (self, ChoicesList = [], texto="Elija", pos = None):

        self.data = None
        self.texto = texto

        self.dialog = gtk.Dialog(self.get_texto(), None, 0)
        self.dialog.set_position(gtk.WIN_POS_MOUSE)

        vbox = gtk.VBox(False, 5)
        vbox.set_border_width(8)
        self.dialog.vbox.pack_start(vbox, False, False, 0)

        # Carga de los botones
        I = 0
        for choice in ChoicesList:
            boton = gtk.Button(label = choice)
            boton.connect("clicked", self.ChoicesCallback, choice)
            #~ boton.connect("clicked", self.ChoicesCallback, str(I))
            vbox.pack_start(boton)
            I+=1

        sepa = gtk.HSeparator()
        vbox.pack_start(sepa)
        # Carga del boton cancelar
        cancelBtn = gtk.Button(label ="Cancelar")
        cancelBtn.connect("clicked", self.ChoicesCallback, "Cancel")
        #~ cancelBtn.connect("clicked", self.ChoicesCallback, str(-1))

        vbox.pack_end(cancelBtn)

        self.dialog.show_all()
        response = self.dialog.run()

        return None

    def ChoicesCallback(self, widget, data = None):
        self.data = data
        self.dialog.destroy()
        return None


    def dialogo(self):
        return self.data

    def set_texto(self, texto):
        self.texto = texto
        return None

    def get_texto(self):
        return self.texto

# -------------------------------------------------- fin clase Choices
#
#
#
#
# -------------------------------------------------- class ArchivoDeEntrada.
class ArchivoDeEntrada():

    def __init__(self, filename = ''):

        self.filename = filename

        return None


    def set_filename(self, filename):
        self.filename = filename
        return None

    def get_filename(self):
        return self.filename

    def set_lines(self, lines):
        self.lines = lines
        return None


    def get_lines(self):

        print 'filename=',self.get_filename()

        if self.get_filename() == '' or self.get_filename() == None:
            raise Exception('No filename to get data from.')

        txtconf = open(self.get_filename())
        #~ print 'txtconf=',txtconf, ' type :',type(txtconf)
        matrix = []

        #~ lines = txtconf.readlines(100000)
        #~ print 'lines=',lines
        lines = txtconf.readlines(10000000)

        if lines == None:
            print 'no lines,break'
            return None
        else:
            return lines


    def chooseFile(self, dialogTitle = ''):
    # ---
    # choose file dialog.
        fileChooser = gtk.FileChooserDialog(dialogTitle, None, 0,
        (gtk.STOCK_OK, gtk.RESPONSE_OK,
        "_Cancel", gtk.RESPONSE_CANCEL))

        fileChooser.show_all()

        response = fileChooser.run()

        if response == gtk.RESPONSE_OK:
            print 'Click en ok'

            okStatus = True
            fileIn = fileChooser.get_filename()
            #~ print 'nameIn=',nameIn
            #~ print 'nameIn[0]=',nameIn[0]
            fileChooser.destroy()

            print 'fileIn=',fileIn

            self.set_filename(fileIn)
            return self
            #~ return fileIn, True, True
        else:
            #~ howwas = False
            print 'Click en cancel'
            fileChooser.destroy()

            return None     #, False, None


    # ------------------------- used for data input.
    def getData(self, header = 0, separador = '\t'):

        print 'filename=',self.get_filename()

        if self.get_filename() == '' or self.get_filename() == None:
            raise Exception('No filename to get data from.')

        txtconf = open(self.get_filename())
        #~ print 'txtconf=',txtconf, ' type :',type(txtconf)
        matrix = []

        #~ lines = txtconf.readlines(100000)
        #~ print 'lines=',lines
        lines = txtconf.readlines(10000000)

        if lines == None:
            print 'no lines,break'
            return None
        else:
            self.set_lines(lines)
            print 'len(lines)=',len(lines)

        #~ print 'lines='
        #~ for line in lines:
            #~ print line

        #~ found = False

        I = 0
        while I<header:
            I += 1


        line = lines[I]

        numbers = string.split(line,separador)
        #~ print 'numbers = ',np.asanyarray(numbers,dtype=float)

        cols = len(numbers)

        matrix = np.zeros((len(lines)-header,len(numbers)),dtype=float)

        matrix[0,:] = np.asanyarray(numbers,dtype=float)
        #~ print 'matrix[0,:] =',matrix[0,:]
        I += 1  # contador por lÃ­neas del archivo.
        J = 1   # contador por lÃ­neas de la matriz.

        while I<len(lines):

            line = lines[I]
            numbers = string.split(line,separador)
            if len(numbers) == cols:
                matrix[J,:] = np.asanyarray(numbers,dtype=float)
                #~ print 'matrix[',J,',:]=',matrix[J,:]
                J += 1
            I += 1

        txtconf.close()

        return matrix
# -------------------------------------------------- end of class ArchivoDeEntrada.
#
#
#
#
#
# -------------------------------------------------- clase ModelClassWriter.
class ModelClassWriter():

    def __init__(self, lines = '', debug = False):

        self.lines = lines
        self.debug = debug
        self.keys = dict(CLASS=self.headerWriter, ATTRIBUTES=self.settersAndGettersWriter, INDEPVAR=self.indepVarWriter, METHOD=self.methodsWriter, EVAL=self.evalWriter)
        self.keysOrder = ['CLASS','ATTRIBUTES','INDEPVAR','METHOD','EVAL']
        self.attrsYmethods = dict(CLASS=[], ATTRIBUTES=[], INDEPVAR=[], METHOD=[], EVAL=[])
        self.comments = dict(CLASS=[], ATTRIBUTES=[], INDEPVAR=[], METHOD=[], EVAL=[])
        self.currentKey = None
        self.classText = None

        return None

    # ---------------------------------- setters y getters.
    def set_lines(self, lines):
        self.lines = lines
        return None

    def get_lines(self):
        return self.lines


    def set_debug(self,debug):
        self.debug = debug
        return None

    def get_debug(self):
        return self.debug


    def set_attrsYmethods(self,attrsYmethods):
        self.attrsYmethods = attrsYmethods
        return None

    def get_attrsYmethods(self):
        return self.attrsYmethods


    def set_comments(self,comments):
        self.comments = comments
        return None

    def get_comments(self):
        return self.comments


    def get_keys(self):
        return self.keys

    def get_keysOrder(self):
        return self.keysOrder


    def set_currentKey(self, currentKey):
        self.currentKey = currentKey
        return None

    def get_currentKey(self):
        return self.currentKey


    def set_classText(self, classText):
        self.classText = classText
        return None

    def get_classText(self):
        return self.classText


    def get_codeText(self):
        texto = self.get_classText()
        codeText = ''
        for line in texto:
            codeText = codeText + line + '\n'
        
        return codeText


    # ---------------------------------- otros métodos.
    def write(self, debug=False):

        if not(debug): debug = self.get_debug()

        classText = []

        # buscar por palabra clave hasta la siguiente palabra clave
        keys = self.get_keys().keys()

        attrsYmethods = self.get_attrsYmethods()
        comments = self.get_comments()   

        L=0
        for rawLine in self.get_lines():

            line = rawLine.replace('\n','').rstrip()
            if debug: print 'linea=',L, 'current key:',self.get_currentKey()

            line = string.split(line,'#')[0]
            
            
            if '@' in line:
                for I in range(0,len(keys)):
                    if debug: print 'Linea: '+str(L)+'|'+', Clave:'+keys[I]+'|line:'+line

                    if keys[I] in line:
                        self.set_currentKey(keys[I])
                        if debug: print 'linea=',L,' cambio de current key=',self.get_currentKey()

            else:
                if not(self.get_currentKey() == None) and (self.get_currentKey()!='EVAL') and (self.get_currentKey()!='METHOD'):
                    if debug: print line
        
                    items1 = string.split(line,'//')
                    items = string.split(items1[0],',')
                    lista = attrsYmethods[self.get_currentKey()]

                    for item in items: # acá se suman de a uno los atributos o métodos
        
                        if item.strip() != '': lista.extend([item.strip()])

                    if debug: print 'antes de setear attrsYmethods: '
                    if debug: print 'current key:',self.get_currentKey(), 'lista=',lista
                    attrsYmethods[self.get_currentKey()] = lista
                    if len(items1) > 1:        
                        comment = items1[1]
                    else:
                        comment = ''
                    comments[str(self.get_currentKey())+item.strip()] = comment
                    if self.get_debug(): print 'comment: ',comment
                else:
                    try:
                        lista = attrsYmethods[self.get_currentKey()]
                        if self.get_debug(): print 'en write, line es:',line
                        if line != '': lista.extend([line])
                    except:
                        pass

            L+=1

        self.set_attrsYmethods(attrsYmethods)
        self.set_comments(comments)
        if debug:
            print
            print
            print
            print
            print
            print
            print '---------------------------------'
            print 'claves del dict de claves:', self.get_keys().keys()
            print '---------------------------------'
            print
            print

        clavesEnOrden = self.get_keysOrder()

        for key in clavesEnOrden:
            lista = self.get_attrsYmethods()[key]
            if debug:
                print key,lista
                print '==='
            for accion in clavesEnOrden:
                self.get_keys()[accion]()

                #~ if debug: print item
            #~ for item in lista:
                #~ print item

        if debug: print '---------------------------------'

        classText = self.get_classText()

        return classText


    def headerWriter(self):
        if self.get_debug(): print 'headerWriter'

        self.set_classText([])  # para empezar.

        lines = []

        # ------------------------------------------------------- Header
        lista = self.get_attrsYmethods()['CLASS']
        classNameAndType = lista[0]

        classType = ''

        if ('=' in classNameAndType):
            dummy,name = string.split(classNameAndType,'=')
            modelName = name.strip()
        else:
            modelName = classNameAndType.strip()

        blankLine = ''

        lines.append('#!usr/bin/python')
        lines.append('# -*- coding: latin-1 -*-')
        lines.append(blankLine)
        lines.append('import numpy as np')
        lines.append(blankLine)

        lines.append('class Model(object):')
        lines.append(blankLine)


        inits = '    def __init__(self'

        attribs = self.get_attrsYmethods()['ATTRIBUTES']

        # ------------------------------------------------------- Definiciones
        for attrib in attribs:
            if ('=' in attrib):                
                [attribName,value] = attrib.split('=')
                
                if attribName.strip() == self.get_attrsYmethods()['INDEPVAR'][0]:
                    value = '['+value.strip()+']'
                
                attrib = attribName+' = '+value
            else:
                if attrib.strip() == self.get_attrsYmethods()['INDEPVAR'][0]:
                    attrib = attrib.strip()+ '= [0.0]'  # porque es la variable independiente.
                
            inits = inits+', '+attrib.strip()
            
        inits = inits+', name=None, parent = None):'
        lines.append(inits)

        lines.append(blankLine)
    
        lines.append('        self.Id = None')
        lines.append('        self.parentId = None')
        lines.append('        self.parent = parent')
        lines.append('        self.name = name                                # nombre de la ecuación, renombrable.')
        lines.append(blankLine)    
        lines.append('        self.model_name = "'+modelName+'"')
        lines.append(blankLine)


        # ------------------------------------------------------- Diccionarios.
        lines.append('    '+'    '+'# ------------------- Dictionaries.')
        setget = ['set','get']
        for what in setget:

            line1 = '    '+'    '+'self.dict_'+what+'ters = dict('
            if len(attribs)>0:
                attrib = attribs[0].strip()
                if ('=' in attrib):
                    [attrib,valor] = string.split(attrib,'=')

                if self.get_debug(): print attrib
                line1 = line1+attrib.strip()+' = self.'+what+'_'+attrib.strip()

            if len(attribs)==1:
                line1 = line1+')'
            else:                
                if attrib != attribs[-1]:
                    line1 = line1+','
                else:
                    line1 = line1+')'

            lines.append(line1)

            line = ''

            for attrib in attribs:
                if not(attrib == attribs[0]):

                    if ('=' in attrib):
                        [elAttrib,valor] = string.split(attrib,'=')
                    
                    #~ line = '    '+'    '+'    '+'    '+attrib.strip()+' = self.'+what+'_'+attrib.strip()+','
                    line = '    '+'    '+'    '+'    '+elAttrib.strip()+' = self.'+what+'_'+elAttrib.strip()

                if (attrib == attribs[-1]):
                    #~ aux = line[0:-1]
                    #~ line = aux+')'
                    line = line+')'
                else:
                    if line != '':
                        line = line+','

                if not (line == ''):  lines.append(line)

            lines.append(blankLine)

        lines.append('    '+'    '+'# ------------------- Attributes.')

        for attrib in attribs:  # acá le saca o no las inicializaciones.
            if ('=' in attrib):
                [attrib,valor] = string.split(attrib,'=')
                #~ print 'attrib y valor=',attrib,valor

            lines.append('    '+'    '+'self.'+attrib+' = '+attrib)

        # atributos que siempre van.
        dictUpdates = """        self.dict_setters.update(dict(name = self.set_name,
                parentId = self.set_parentId,
                type = self.set_type))

        self.dict_getters.update(dict(name = self.get_name,
                parentId = self.get_parentId,
                type = self.get_type))

        """
        lines.append(blankLine)
        lines.append(blankLine)
        lines.append(dictUpdates)

        # UIkeys y UIlabels van acá.
        lines.append("        # UIkeys list.")

        UIkeys = '    '+'    '+'self.dict_UIkeys = ['
        keyItems = []
        if len(attribs)>0:
            for attrib in attribs:
                if attrib != attribs[0]:
                    UIkeys = UIkeys + ","

                if ('=' in attrib):
                    [attrib,valor] = string.split(attrib,'=')
                UIkeys = UIkeys + "'"+attrib.strip()+"'"
                keyItems.append(attrib.strip())

        UIkeys = UIkeys+']'
        lines.append(UIkeys)

        lines.append(blankLine)
        lines.append("        # UIlabels list.")
        
        if len(attribs)>0:
            for attrib in attribs:
                
                if ('=' in attrib):
                    [elAttrib,valor] = string.split(attrib,'=')
                #~ dictEntry = elAttrib+ " = "+'"'+self.get_comments()['ATTRIBUTES'+attrib]+'"'
                dictEntry = elAttrib+ " = "+'"'+self.get_comments()['ATTRIBUTES'+attrib.strip()]+'"'
                if attrib == attribs[0]:
                    dictEntry = "        self.dict_UIlabels = dict(" + dictEntry
                if attrib != attribs[-1]:
                    dictEntry = dictEntry + ','
                if attrib != attribs[0]:
                    dictEntry = "                "+dictEntry
                if attrib == attribs[-1]:
                    dictEntry = dictEntry + ")"
                lines.append(dictEntry)

        lines.append(blankLine)
        lines.append('    '+'    '+'return None')
        lines.append(blankLine)

        self.set_classText(lines)

        return None


    def settersAndGettersWriter(self):
        if self.get_debug(): print 'settersAndGettersWriter'

        blankLine = ''
        lines = self.get_classText()
        attribs = self.get_attrsYmethods()['ATTRIBUTES']

        # ------------------------------------------------------- Setters y getters
        lines.append('    '+'# --------------------------------------------- Dictionaries getters and ATTRIBUTESs managing methods.')

        dictSettersAndGetters = """    def get_dict_getters(self):
        return self.dict_getters

    def get_dict_setters(self):
        return self.dict_setters


    def get_dict_UIkeys(self):
        return self.dict_UIkeys

    def get_dict_UIlabels(self):
        return self.dict_UIlabels


    def get_UILabels(self):
        orden = self.get_dict_UIkeys()
        labelsTxt = []
        labels = self.get_dict_UIlabels()
        for item in orden:
             labelsTxt.append(labels[item])
        return labelsTxt


    def get_ATTRIBUTESs(self):
        return self.get_dict_setters().keys()

    def set_ATTRIBUTES(self, ATTRIBUTES, newValue):
        changed = False
        try:
            oldValue = self.get_dict_getters()[ATTRIBUTES]
            if oldValue != newValue:    changed = True
            self.get_dict_setters()[ATTRIBUTES] = newValue
            self.get_parent().update(self.get_name())
            return True
        except:
            return False

        """

        lines.append(dictSettersAndGetters)
        lines.append('    '+'# --------------------------------------------- Setters and getters')

        for attrib in attribs:  # acá le saca o no las inicializaciones.
            if ('=' in attrib):
                [attrib,valor] = string.split(attrib,'=')
                #~ print 'attrib y valor=',attrib,valor

            attrib = attrib.strip()

            line1 = '    '+'def set_'+attrib+'(self, '+attrib+'):'
            line2 = '    '+'    '+'self.'+attrib+' = '+attrib
            line3 = '    '+'    '+'return None'

            line4 = '    '+'def get_'+attrib+'(self):'
            line5 = '    '+'    '+'return self.'+attrib

            lines.append(line1)
            lines.append(line2)
            lines.append(line3)
            lines.append(blankLine)
            lines.append(line4)
            lines.append(line5)
            lines.append(blankLine)
            lines.append(blankLine)

        self.set_classText(lines)

        return None


    def methodsWriter(self):
        if self.get_debug(): print 'methodsWriter'

        blankLine = ''
        lines = self.get_classText()

        #~

        methods = self.get_attrsYmethods()['METHOD']

        #~ print 'methods=',methods

        for methodLine in methods:

            '''
            #~ print ' --- metodo:',method

            line1 = '    '+'def '+method.strip()+'(self'

            line1 = line1+'):'

            line2 = '    '+'    '+'return None'

            lines.append(line1)
            #~ lines.append(blankLine)
            lines.append(line2)
            lines.append(blankLine)
            lines.append(blankLine)
            '''
            lines.append('    '+methodLine)

        lines.append(blankLine)
        lines.append(blankLine)
        
        # ------------------------------------- métodos auxiliares requeridos.
        metodosAuxiliares = """    def set_model_name(self, model_name):
        self.model_name = model_name
        return None

    def get_model_name(self):
        return self.model_name


    def set_Id(self, Id):           # este método se utiliza al deshidratar y rehidratar los objetos.
        self.Id = Id
        return None

    def get_Id(self):               # este método se utiliza al deshidratar y rehidratar los objetos.
        return self.Id


    def set_name(self, name):           # este método se utiliza durante el uso normal del objeto.
        self.name = name
        return None

    def get_name(self):                 # este método se utiliza durante el uso normal del objeto.
        return self.name


    def set_parent(self, parent):       # este método se utiliza durante el uso normal del objeto.
        self.parent = parent
        return None

    def get_parent(self):               # este método se utiliza durante el uso normal del objeto.
        return self.parent


    def set_parentId(self, parentId):# este método se utiliza al deshidratar y rehidratar los objetos.
        self.parentId = parentId
        return None

    def get_parentId(self):          # este método se utiliza al deshidratar y rehidratar los objetos.
        return self.parentId


    def set_type(self, type):
        # no se setea, es un método dummy
        return None
        
    def get_type(self):                 # este método se utiliza al deshidratar los objetos y sirve como clave para rehidratarlos.
        return str(type(self)).strip()

    # --------------------------------------------- Methods
    def is_equation(self):
        return True


    def set_debug(self, debug):
        self.debug = debug
        return None

    def get_debug(self):
        return self.debug


    def get_data_as_dict(self):

        self.dic = dict()
        getters = self.get_dict_getters()
        for clave in getters.keys():        # devuelve las claves o valores de los atributos en una lista.
            attrib = getters[clave]()       # devuelve el valor (u objeto) del getter.
            if type(attrib) == type([1,2]):
                lista = []
                for item in attrib:
                    try:
                        obj = item.get_data_as_dict()
                        lista.append(obj)
                    except:
                        lista.append(item)
                self.dic[clave] = lista
            else:
                try:
                    obj = attrib.get_data_as_dict()
                    self.dic[clave] = obj
                except:
                    self.dic[clave] = attrib

        return self.dic        
        
        """
        
        lines.append(metodosAuxiliares)

        self.set_classText(lines)

        return None

    def indepVarWriter(self):

        lines = self.get_classText()
        indepVarName = self.get_attrsYmethods()['INDEPVAR']

        if len(indepVarName) > 1:
            indepVarName = [indepVarName[0]]

        indepVarName = indepVarName[0].strip()

        blankLine = ''
        line0 = '    '+'# Independent variable.'
        line1 = '    '+'def set_indepVar(self, value):'
        line2 = '    '+'    '+'self.set_'+indepVarName+' = value'
        line3 = '    '+'    '+'return None'

        line4 = '    '+'def get_indepVar(self):'
        line5 = '    '+'    '+'return self.get_'+indepVarName+'()'


        lines.append(line0)
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(blankLine)
        lines.append(line4)
        lines.append(line5)
        lines.append(blankLine)
        lines.append(blankLine)


        self.set_classText(lines)
        return None

    def evalWriter(self):

        lines = self.get_classText()
        lista = self.get_attrsYmethods()['EVAL']    # este devuelve automáticamente todas las líneas sin tabs.

        evalEncab = """def eval(self, indepVar=None):

        if indepVar == None:
            indepVar = self.get_indepVar()
            
        x_out = []
        y_out = []
        """

        lines.append('    '+evalEncab)
        
        attribs = self.get_attrsYmethods()['ATTRIBUTES']

        for attrib in attribs:  # acá le saca o no las inicializaciones.
            if ('=' in attrib):
                [attrib,valor] = string.split(attrib,'=')


            attrib = attrib.strip()

            line = '        '+attrib+' = self.get_'+attrib+'()'
            lines.append(line)
        lines.append('')


        for item in lista:
            #~ print item
            lines.append('        '+item)
            
        lines.append('')
        lines.append('        return x_out, y_out')

        self.set_classText(lines)
        return None

# --------------------------------
#
#
#
#
#


if __name__ == "__main__":

    print "Iniciando programa."
    Controller()
    gtk.main()

#eof.-
