// =====================================================================
//  TRIXIG+  —  parametrisk CAD-modell
//  GK4 Designmetodikk, AHO 2026
//
//  Approksimasjon av IKEA TRIXIG (3,6 V, art.nr. 305.469.09) med
//  modifikasjonane som er foreslått i Trixig+:
//      - reparerbar kapsling (M3-skruekrager)
//      - utskiftbart batterirom (18650-celle)
//      - asymmetrisk retningsbryter
//      - statuslysstrip i bakkant
//
//  Slik bruker du fila:
//      1) Opne i OpenSCAD (gratis, openscad.org).
//      2) Trykk F5 for hurtigvising, F6 for full render.
//      3) Eksporter til STL: Fil → Eksporter → Eksporter som STL.
//      4) Importer STL i Fusion 360 (Innsett → Mesh → Importer).
//      5) Konverter til BRep om ynskt: Mesh → Modify → Convert Mesh.
//
//  Strukturen er modulær. Du kan kommentere ut delar du ikkje treng.
// =====================================================================


// ---------- HOVUDPARAMETRE (juster fritt) ----------------------------

// Hovudhus (motor + bitsfeste)
front_length      = 90;     // lengde frå spiss av bitsfeste til vinkel
front_diameter    = 38;     // diameter på motorkammeret
nose_diameter     = 22;     // diameter ved bitsfestet (taper)
nose_length       = 18;     // lengde av nese-tapen

// Grep
handle_length     = 95;     // lengde frå vinkel til botn av grepet
handle_width      = 36;     // bredde over tommel
handle_depth      = 28;     // djupne (front til bak) av grepet
handle_angle      = 70;     // vinkel mellom hovudhus og grep (grader frå vertikal)
                            // 70° gir ein open vinkel på ca. 110° mellom delane

// Avtrekker
trigger_length    = 32;
trigger_width     = 14;
trigger_depth     = 8;
trigger_y_offset  = 22;     // kor langt nede frå vinkelen avtrekkeren startar

// Asymmetrisk retningsbryter (Trixig+-feature)
dirsw_width       = 24;
dirsw_height      = 18;
dirsw_depth       = 6;

// Statuslysstrip
status_strip_w    = 30;
status_strip_h    = 4;

// USB-C-port
usb_w             = 9.5;
usb_h             = 3.2;

// M3 reparerbarheit-skruer (Trixig+-feature)
m3_count          = 6;
m3_clearance      = 3.4;    // hol gjennom toppskall
m3_head_dia       = 6.5;
m3_head_depth     = 2.5;

// 18650 batterikammer (Trixig+-feature)
cell_diameter     = 18.6;   // 18650 nominelt 18,6 mm med toleranse
cell_length       = 65.5;

// Render-oppløysing
$fn = 80;                   // hev til 120+ for endeleg STL


// ---------- HOVUDBYGG -------------------------------------------------

module trixig_plus_assembly() {
    color("DimGray") trixig_main_body();
    color("LightSlateGray") trigger();
    color("DarkGray") direction_switch_asymmetric();
    color("Crimson") status_strip_lights();
    color("Silver") bit_holder();
}


// ---------- HOVUDHUS --------------------------------------------------

module trixig_main_body() {
    difference() {
        union() {
            front_section();
            handle_section();
        }
        // Avtrekkar-utskjering
        translate([0, -trigger_depth/2, -trigger_y_offset])
            rotate([0, 0, 0])
            cube([trigger_width + 4, trigger_depth + 4, trigger_length + 4], center = true);

        // Asymmetrisk retningsbryter-utskjering
        translate([0, -handle_depth/2 - 1, -trigger_y_offset - 30])
            cube([dirsw_width + 1, dirsw_depth + 4, dirsw_height + 1], center = true);

        // USB-C-port (botn av grepet)
        translate([0, 0, -trigger_y_offset - handle_length + 10])
            rotate([90, 0, 0])
            cube([usb_w, usb_h, handle_depth + 2], center = true);

        // Statuslysstrip (bak)
        translate([0, handle_depth/2 - 1, -trigger_y_offset - handle_length/2 - 10])
            rotate([90, 0, 0])
            cube([status_strip_w, status_strip_h, 4], center = true);

        // Reparerbarheit-skruer (Trixig+)
        m3_screw_pattern();

        // Batterikammer (utskiftbart)
        translate([0, 0, -trigger_y_offset - handle_length/2])
            rotate([0, 0, 90])
            cylinder(d = cell_diameter, h = cell_length, center = true);
    }
}


// ---------- FRONTSEKSJON (motorkammer + nese) ------------------------

module front_section() {
    // Hovudsylinder for motor
    rotate([90, 0, 0])
        cylinder(d = front_diameter, h = front_length, center = true);

    // Nese (taper ned mot bitsfeste)
    translate([0, front_length/2, 0])
        rotate([90, 0, 0])
        cylinder(d1 = front_diameter, d2 = nose_diameter, h = nose_length, center = false);
}


// ---------- GREP (vinkla bak/ned) ------------------------------------

module handle_section() {
    rotate([handle_angle, 0, 0])
        translate([0, 0, -handle_length/2])
        hull() {
            cube([handle_width, handle_depth, 0.1], center = true);
            translate([0, 0, -handle_length])
                cube([handle_width * 0.85, handle_depth * 0.9, 0.1], center = true);
        }
}


// ---------- AVTREKKER -------------------------------------------------

module trigger() {
    translate([0, -trigger_depth/2 - handle_depth/2 + 4, -trigger_y_offset])
        cube([trigger_width, trigger_depth, trigger_length], center = true);
}


// ---------- ASYMMETRISK RETNINGSBRYTER (Trixig+) ---------------------
// Den eine sida konveks med pil framover, den andre konkav med pil bakover.
// Skal vere taktilt og visuelt forskjellig — sjå rapporten kap. 10.2.

module direction_switch_asymmetric() {
    translate([0, -handle_depth/2 - dirsw_depth/2 + 1, -trigger_y_offset - 30]) {
        // Konveks side (forover)
        translate([-dirsw_width/4, 0, 0])
            difference() {
                cube([dirsw_width/2, dirsw_depth, dirsw_height], center = true);
                // Konvekst utbygg = trekk frå negativ kule
                translate([0, dirsw_depth/2, 0])
                    sphere(d = dirsw_height * 1.2);
            }
        // Konkav side (bakover)
        translate([dirsw_width/4, 0, 0])
            difference() {
                cube([dirsw_width/2, dirsw_depth, dirsw_height], center = true);
                // Konkav fordjuping
                translate([0, -dirsw_depth/4, 0])
                    sphere(d = dirsw_height * 0.8);
            }
        // Pil-relieff (forenkla — du kan endre i CAD)
        translate([-dirsw_width/4, dirsw_depth/2, 0])
            arrow_relief(direction = 1);
        translate([dirsw_width/4, -dirsw_depth/4, 0])
            arrow_relief(direction = -1);
    }
}

module arrow_relief(direction = 1) {
    // Trekantar som angir retning
    rotate([90, 0, 0])
        linear_extrude(0.5)
        polygon([
            [direction * 4, 0],
            [-direction * 2, 3],
            [-direction * 2, -3]
        ]);
}


// ---------- STATUSLYSSTRIP --------------------------------------------

module status_strip_lights() {
    for (i = [0:3]) {
        translate([
            -status_strip_w/2 + 6 + i * 6,
            handle_depth/2 + 0.5,
            -trigger_y_offset - handle_length/2 - 10
        ])
        rotate([90, 0, 0])
        cylinder(d = 2.5, h = 1, center = true);
    }
}


// ---------- BITSFESTE -------------------------------------------------

module bit_holder() {
    translate([0, front_length/2 + nose_length, 0])
        rotate([90, 0, 0]) {
            // Sekskantet 1/4'' bitsfeste
            cylinder(d = 11, h = 12, $fn = 6);
        }
}


// ---------- M3 REPARERBARHEIT-SKRUER ---------------------------------
// Seks M3-hol som går gjennom skallet, distribuert som i ekte produktet.

module m3_screw_pattern() {
    positions = [
        [ 14,  10, -trigger_y_offset - 5 ],
        [-14,  10, -trigger_y_offset - 5 ],
        [ 14,   0, -trigger_y_offset - 35],
        [-14,   0, -trigger_y_offset - 35],
        [ 12, -10, -trigger_y_offset - 75],
        [-12, -10, -trigger_y_offset - 75]
    ];
    for (p = positions) {
        translate(p)
            rotate([handle_angle, 0, 0]) {
                // Klaringshol
                cylinder(d = m3_clearance, h = handle_depth + 2, center = true);
                // Skruehovud-fordjuping (Torx T10 sokkelhovud)
                translate([0, 0, handle_depth/2 - m3_head_depth + 0.5])
                    cylinder(d = m3_head_dia, h = m3_head_depth + 1, center = false);
            }
    }
}


// ---------- HOVUDKALL ------------------------------------------------

trixig_plus_assembly();


// ---------- VALFRIE EKSTRA --------------------------------------------
// Fjern // for å aktivere:

// Vis berre eit halvskall (snitt langs YZ-planet) — nyttig for å sjå innvendig:
// difference() {
//     trixig_plus_assembly();
//     translate([100, 0, -200]) cube([200, 200, 400]);
// }

// Eksporter berre øvre skall:
// intersection() {
//     trixig_main_body();
//     translate([0, -100, -200]) cube([200, 200, 400]);
// }

// =====================================================================
//  Slutten av fil. Sjå Prototypedokumentasjon.md for byggjeoppskrift.
// =====================================================================
