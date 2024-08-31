from manim import *

import re
import mendeleev
import numpy as np
import time
import json
import os
import random
from copy import deepcopy
from colormap import hex2rgb, rgb2hex
from pint import Q_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List

def log_interp(xx, yy, kind='linear'):
    logx = np.log10(xx)
    logy = np.log10(yy)
    lin_interp = sp.interpolate.interp1d(logx, logy, kind=kind)
    log_interp1d = lambda zz: np.power(10.0, lin_interp(np.log10(zz)))
    return log_interp1d


def calc_Q_value(parents: list, daughters: list):
    parents_mass = sum([p.mass.to("amu") for p in parents])
    daughters_mass = sum([d.mass.to("amu") for d in daughters])
    Q = (parents_mass - daughters_mass) * Q_(931.5, "MeV / amu")
    return Q.to("MeV")


class Proton():
    """
    Helper class for rendering and working with protons.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render a Proton.
        """
        proton_circle = Circle(
            radius=0.4,
            color=RED,
        ).set_fill("#7d3129", opacity=1.0)
        proton_tex = Tex(r"$p$")
        proton = VGroup(proton_circle, proton_tex)
        return proton


    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(1.00727647, "amu")


class Neutron():
    """
    Helper class for rendering and working with neutrons.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render a Neutron.
        """
        neutron_circle = Circle(
            radius=0.4,
            color=GREEN,
        ).set_fill("#416033", opacity=1.0)
        neutron_tex = Tex(r"$n$")
        neutron = VGroup(neutron_circle, neutron_tex)
        return neutron


    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(1.00866492, "amu")


class Electron():
    """
    Helper class for rendering and working with electrons.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render an Electron.
        """
        electron_circle = Circle(
            radius=0.4,
            color=BLUE,
        ).set_fill("#2c626e", opacity=1.0)
        electron_tex = Tex(r"$e$")
        electron = VGroup(electron_circle, electron_tex)
        return electron


    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(0.00054858, "amu")


class AlphaParticle():
    """
    Helper class for rendering and working with alphas.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render an AlphaParticle.
        """
        alpha_circle = Circle(
            radius=0.4,
            color=RED,
        ).set_fill("#7d3129", opacity=1.0)
        alpha_tex = Tex(r"$\alpha$")
        alpha = VGroup(alpha_circle, alpha_tex)
        return alpha

    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(4.00150618, "amu")


class BetaMinusParticle():
    """
    Helper class for rendering and working with beta-minus particles.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render an BetaMinusParticle.
        """
        beta_m_circle = Circle(
            radius=0.4,
            color=BLUE,
        ).set_fill("#2c626e", opacity=1.0)
        beta_m_tex = Tex(r"$\beta^-$")
        beta_m = VGroup(beta_m_circle, beta_m_tex)
        return beta_m

    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(0.00054858, "amu")


class BetaPlusParticle():
    """
    Helper class for rendering and working with beta-plus particles.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render an BetaPlusParticle.
        """
        beta_p_circle = Circle(
            radius=0.4,
            color=RED,
        ).set_fill("#7d3129", opacity=1.0)
        beta_p_tex = Tex(r"$\beta^+$")
        beta_p = VGroup(beta_p_circle, beta_p_tex)
        return beta_p

    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(0.00054858, "amu")


class GammaParticle():
    """
    Helper class for rendering and working with gamma particles.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render an GammaParticle.
        """
        gamma_circle = Circle(
            radius=0.35,
            color=YELLOW,
        ).set_fill("#B0A500", opacity=1.0)
        gamma_tex = Tex(r"$\gamma$")
        gamma = VGroup(gamma_circle, gamma_tex)
        return gamma

    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(0, "amu")


class NeutrinoParticle():
    """
    Helper class for rendering and working with neutrinos.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render a Neutrino Particle.
        """
        neu_circle = Circle(
            radius=0.35,
            color="#4e1752",
        ).set_fill(PINK, opacity=1.0)
        neu_tex = Tex(r"$\nu_e$")
        neu = VGroup(neu_circle, neu_tex)
        return neu

    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(0, "amu")


class AntiNeutrinoParticle():
    """
    Helper class for rendering and working with antineutrinos.
    """
    @property
    def sprite(self) -> VGroup:
        """
        Returns a VGroup to render a AntiNeutrinoParticle.
        """
        antineu_circle = Circle(
            radius=0.35,
            color="#6e4b05",
        ).set_fill(ORANGE, opacity=1.0)
        antineu_tex = Tex(r"$\bar{\nu}_e$")
        antineu = VGroup(antineu_circle, antineu_tex)
        return antineu

    @property
    def mass(self) -> Q_:
        """
        Returns mass in amu.
        """
        return Q_(0, "amu")


class Isotope():
    """
    Helper class for rendering and working with isotopes.
    """
    def __init__(self, element: str, mass_number: int, fill_color: str="#FFFFFF", excited=False):
        self.element = element
        self.mass_number = mass_number
        self.fill_color = fill_color
        self.excited = excited

    def __call__(self):
        return self.sprite


    def __str__(self) -> str:
        """
        Stringify isotope
        """
        return f"{self.element}-{self.mass_number}"

    def __repr__(self) -> str:
        return f"Isotope({self.element}-{self.mass_number})"

    @property
    def _mendeleev_iso(self) -> mendeleev.Isotope:
        """
        Returns the mendeleev.Isotope object for the Isotope, should not be called in top level code.
        """
        for iso in mendeleev.element(self.element).isotopes:
            if iso.mass_number == self.mass_number:
                return iso


    @property
    def sprite(self, radius=1.0) -> VGroup:
        """
        Returns a Vgroup to render the Isotope.
        """
        # Check that the fill color was provided in hexidecimal form
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){2}$', self.fill_color)
        if match is None:
            raise ValueError(f"Isotope {self.element}-{self.mass_number}'s fill_color is not a valid hex color")

        # Darken the fill color to make the border color
        border_color = rgb2hex(*[int(col * 0.6) for col in hex2rgb(self.fill_color)])

        # Isotope name
        iso_str = f"^{{{self.mass_number}}}\\text{{{self.element}}}"
        if self.excited:
            iso_str += r"^*"
        iso_name = MathTex(iso_str)
        iso_name_length = (iso_name.get_right() - iso_name.get_left())[0]

        # Isotope circle
        iso_circle = Circle(
            radius=iso_name_length / 1.6,
            color=border_color
        ).set_fill(self.fill_color, opacity=1.0)

        # Make VGroup
        isotope = VGroup(iso_circle, iso_name)

        # Scale isotope to desired size
        isotope.scale(radius / iso_circle.get_radius())
        return isotope



    @property
    def Z(self) -> int:
        """
        Returns Isotope's atomic number.
        """
        return mendeleev.element(self.element).atomic_number


    @property
    def N(self) -> int:
        """
        Returns number of neutrons in Isotope.
        """
        return self.mass_number - self.Z


    @property
    def A(self) -> int:
        """
        Returns the mass number of the Isotope.
        """
        return self.mass_number


    @property
    def mass(self) -> Q_:
        """
        Returns the mass of the isotope, including electrons.
        """
        return Q_(self._mendeleev_iso.mass, "amu")


    @property
    def half_life(self) -> Q_:
        """
        Return the half life of the isotope. If the isotope is stable, returns an infinite half life.
        """
        if self.is_stable is False:
            return Q_(np.Inf, "seconds")
        else:
            return Q_(self._mendeleev_iso.half_life, self._mendeleev_iso.half_life_unit.replace("y", "year"))


    @property
    def decay_constant(self) -> Q_:
        """
        Return decay constant of the isotope.
        """
        return (np.log(2) / self.half_life).to("1 / seconds")


    def get_xs(self, incident_particle, cross_section):
        """
        This function scrapes publically available ENDF files for a desired cross-section.
        Once a cross section is pulled, it is saved to the cross_sections.json file in the
        repo. In the future if we want the cross sections again, we check the JSON file
        first to see if we have it available to save time.
        """
        # Validate the incident particle
        if incident_particle not in ["n", "g", "p", "d", "t", "a"]:
            raise ValueError(f"Incident particle \"{incident_particle}\" is not supported")

        # Validate the cross section
        if cross_section not in ["total", "elastic_scatter", "inelastic_scatter", "fission", "capture"]:
            raise ValueError(f"Cross section reaction ID for \"{cross_section}\" is not known")

        # First, check the cross sections JSON file to see if we already have what we are looking for
        with open(os.path.join(self.get_xs.__globals__["__file__"], "..", "cross_sections.json")) as json_file:
            xs_data = json.load(json_file)
        cached_xs = xs_data.get(self.element, {}).get(str(self.mass_number), {}).get(cross_section, {})

        # If we have it cached, just use it instead
        if cached_xs != {}:
            xs = {
                "energy": Q_(cached_xs["energy"], "eV"),
                "xs": Q_(cached_xs["xs"], "barn")
            }
            return xs

        # We don't have the desired cross section cached, so we need to scrape ENDF for it.
        print(f"[nuclyr-TFN] Scraping ENDF for {str(self)} {cross_section} cross-section data for particle {incident_particle}")

        # Configure webdriver
        options = webdriver.EdgeOptions()
        options.add_argument("headless")
        driver = webdriver.Edge(options=options)

        # Go to JANIS ENDF website
        driver.get("https://www.oecd-nea.org/janisweb/search/endf")

        # XPaths for entering reaction to get cross sections
        incident_particle_field = "/html/body/div/div/div/div[2]/form/div[1]/div[2]/div/button/span[1]"
        library_field = "/html/body/div/div/div/div[2]/form/div[2]/div[2]/div/button/span[1]"
        element_field = "/html/body/div/div/div/div[2]/form/div[3]/div[2]/div[1]/input"
        mass_number_field = "/html/body/div/div/div/div[2]/form/div[3]/div[3]/div[1]/input"
        xs_field = "/html/body/div/div/div/div[2]/form/div[4]/div[2]/div[1]/span/button/i"
        rxn_field = "/html/body/div/div/div/div[2]/form/div[5]/div[2]/div[1]/span/button/i"
        submit_button = "/html/body/div/div/div/div[2]/form/div[6]/button"

        # Enter incident particle
        driver.find_element(By.XPATH, incident_particle_field).click()
        if incident_particle == "n":
            txt = "Incident neutron data"
        elif incident_particle == "g":
            txt = "Incident gamma data"
        elif incident_particle == "p":
            txt = "Incident proton data"
        elif incident_particle == "d":
            txt = "Incident deuteron data"
        elif incident_particle == "t":
            txt = "Incident triton data"
        elif incident_particle == "a":
            txt = "Incident alpha data"
        driver.find_element(By.XPATH, f"//*[contains(text(), '{txt}')]").click()
        driver.find_element(By.XPATH, incident_particle_field).click()

        # Use ENDF/B-VIII.0
        driver.find_element(By.XPATH, library_field).click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'ENDF/B-VIII.0')]").click()
        driver.find_element(By.XPATH, library_field).click()

        # Enter element
        driver.find_element(By.XPATH, element_field).send_keys(self.element)
        driver.find_element(By.XPATH, element_field).send_keys(Keys.TAB)

        # Enter mass number
        driver.find_element(By.XPATH, mass_number_field).send_keys(self.mass_number)
        driver.find_element(By.XPATH, mass_number_field).send_keys(Keys.TAB)

        # We want cross sections
        driver.find_element(By.XPATH, xs_field).click()
        xs_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), 'MF=3')]"))
        )
        xs_option.click()

        # Enter proper reaction
        if cross_section == "total":
            xs = "1"
        elif cross_section == "elastic_scatter":
            xs = "2"
        elif cross_section == "inelastic_scatter":
            xs = "3"
        elif cross_section == "fission":
            xs = "18"
        elif cross_section == "capture":
            xs = "102"
        driver.find_element(By.XPATH, rxn_field).click()
        rxn_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), 'MT={xs}')]"))
        )
        rxn_option.click()

        # Submit
        driver.find_element(By.XPATH, submit_button).click()

        # Select the proper row
        table = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/table/tbody")
        for row in table.find_elements(By.XPATH, ".//tr"):
            if all(s in row.text for s in [txt, f"{self.element}{self.mass_number}", "ENDF/B-VIII.0", "3", f"MT={xs}"]):
                checkbox = row.find_elements(By.XPATH, ".//input[@type='checkbox']")[0]
                checkbox.click()
                break

        # Query
        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[3]/button").click()

        # Pull up cross section results
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/table/tbody"))
        )

        # Get the row with the cross sections
        for row in table.find_elements(By.XPATH, ".//tr"):
            for col in row.find_elements(By.XPATH, ".//td"):
                if col.text == "Cross section":
                    checkbox_col = row.find_elements(By.XPATH, ".//td")[-1]
                    break
        # Get the checkbox ID for the table
        for element in checkbox_col.find_elements(By.XPATH, '*'):
            if element.text == "T":
                checkbox_id = element.get_attribute("for")
                break
        # Bring up the final xs table
        driver.find_element("id", checkbox_id).click()

        # To limit the amount of data we are dealing with,
        # we will grab 50 interpolated points per decade,
        # evenly spaced logarithmically.
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/table/tbody"))
        )
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset[3]/table[1]/tbody/tr[2]/td/input").click()
        time.sleep(0.25)
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset[3]/table[1]/tbody/tr[3]/td/input").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset[3]/table[1]/tbody/tr[5]/td[1]/input").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset[3]/table[1]/tbody/tr[5]/td[2]/input[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset[3]/table[1]/tbody/tr[5]/td[2]/input[1]").send_keys("50")
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset[3]/p[2]/input").click()
        time.sleep(1.0)

        # Grab the cross section table
        xs_table = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/table/tbody")

        # Check if there are multiple pages
        first_row = xs_table.find_elements(By.XPATH, ".//tr")[0]
        if "Next" in first_row.text:
            multiple_pages = True
            num_pages = int(first_row.text.split()[-1])
        else:
            multiple_pages = False

        # Loop over rows and pages and save results
        page = 1
        rows = xs_table.find_elements(By.XPATH, ".//tr")
        energy_list = list()
        xs_list = list()
        while True:
            for i, row in enumerate(rows):
                # Skip paging rows if there are multiple pages
                if multiple_pages is True and (i == 0 or i == len(rows) - 1):
                    continue
                # Pull energy and cross section from row
                energy_val, xs_val = row.text.split()
                energy_list.append(float(energy_val))
                xs_list.append(float(xs_val))
            # Go to next page, if applicable
            if multiple_pages is True and page < num_pages:
                next_button = xs_table.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div/div[2]/div/table/tbody/tr[1]/td/div/div/a[{page}]")
                next_button.click()
                page += 1
                time.sleep(1.0)
                xs_table = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/table/tbody")
                rows = xs_table.find_elements(By.XPATH, ".//tr")
            else:
                break

        # Save results to cross_sections.json
        new_xs_dict = {
            self.element: {
                str(self.mass_number): {
                    cross_section: {
                        "energy": energy_list,
                        "xs": xs_list
                    }
                }
            }
        }
        if self.element in xs_data:
            if str(self.mass_number) in xs_data[self.element]:
                xs_data[self.element][str(self.mass_number)][cross_section] = new_xs_dict[self.element][str(self.mass_number)][cross_section]
            else:
                xs_data[self.element][str(self.mass_number)] = new_xs_dict[self.element][str(self.mass_number)]
        else:
            xs_data.update(new_xs_dict)
        with open(os.path.join(self.get_xs.__globals__["__file__"], "..", "cross_sections.json"), "w") as json_file:
            json.dump(xs_data, json_file, indent = 4) 

        # Return results
        xs = {
            "energy": Q_(energy_list, "eV"),
            "xs": Q_(xs_list, "barn")
        }
        return xs


class AlphaDecay():
    def __init__(self, parent: Isotope) -> None:
        self.parent = parent

    @property
    def daughter(self) -> Isotope:
        daughter_Z = self.parent.Z - 2
        daughter_A = self.parent.A - 4
        return Isotope(element=mendeleev.element(daughter_Z).symbol, mass_number=daughter_A)

    @property
    def Q(self) -> Q_:
        return calc_Q_value(parents=[self.parent], daughters=[self.daughter, Isotope(element="He", mass_number=4)])

    @property
    def daughter_energy(self) -> Q:
        return (self.Q * (Isotope(element="He", mass_number=4).mass / (self.parent.mass + Isotope(element="He", mass_number=4).mass))).to("MeV")

    @property
    def alpha_energy(self) -> Q:
        return (self.Q * (self.parent.mass / (self.parent.mass + Isotope(element="He", mass_number=4).mass))).to("MeV")


class BetaMinusDecay():
    def __init__(self, parent: Isotope) -> None:
        self.parent = parent

    @property
    def daughter(self) -> Isotope:
        daughter_Z = self.parent.Z + 1
        daughter_A = self.parent.A
        return Isotope(element=mendeleev.element(daughter_Z).symbol, mass_number=daughter_A)

    @property
    def Q(self) -> Q_:
        return calc_Q_value(parents=[self.parent], daughters=[self.daughter, AntiNeutrinoParticle()])


class BetaPlusDecay():
    def __init__(self, parent: Isotope) -> None:
        self.parent = parent

    @property
    def daughter(self) -> Isotope:
        daughter_Z = self.parent.Z - 1
        daughter_A = self.parent.A
        return Isotope(element=mendeleev.element(daughter_Z).symbol, mass_number=daughter_A)

    @property
    def Q(self) -> Q_:
        return calc_Q_value(parents=[self.parent], daughters=[self.daughter, BetaPlusParticle(), BetaPlusParticle(), NeutrinoParticle()])


class GammaDecay():
    def __init__(self, parent: Isotope, excitation_energy: Q_) -> None:
        self.parent = parent
        self.parent.excited = True
        self.excitation_energy = excitation_energy

    @property
    def daughter(self) -> Isotope:
        daughter = deepcopy(self.parent)
        daughter.excited = False
        return daughter

    @property
    def Q(self) -> Q_:
        return self.excitation_energy


# Helper class for a material, which may be composed of many different atoms
class Material():
    def __init__(self, composition: Dict[Isotope, float], fractions: str, density: Q_) -> None:
        assert fractions in ["wt", "at"], "fraction must be either 'wt' or 'at"
        self._composition = composition
        self.fractions = fractions
        self.density = density
        self.composition = self._derive_composition()
        self.atom_densities = self._derive_atom_densities()

    def __repr__(self) -> str:
        compstr = ""
        for iso, afrac in self.composition.items():
            compstr += f"{iso.element}[{afrac.m:.3f}],"
        return f"Material({compstr[:-1]})"

    def _derive_composition(self) -> Dict[Isotope, float]:
        """This helper function derives the atomic fractions of the material
        """
        if self.fractions == "at":
            return self._composition
        else:
            comp = dict()
            for iso, wfrac in self._composition.items():
                comp[iso] = (wfrac / iso.mass) / sum([v / k.mass for k, v in self._composition.items()])
        return comp

    def _derive_atom_densities(self) -> Dict[Isotope, Q_]:
        """This helper function derives the atomic densities within the material
        """
        unit_density = self.density / self.unit_mass
        atom_densities = dict()
        for iso, afrac in self.composition.items():
            atom_densities[iso] = (unit_density * afrac).to("1 / (barn * cm)")
        return atom_densities

    @property
    def unit_mass(self) -> Q_:
        mass = Q_(0, "amu")
        for iso, afrac in self.composition.items():
            mass += iso.mass * afrac
        return mass

# Helper class to simulate a neutron
class NSim():
    def __init__(self, E: Q_, r: List[float]=[0.0, 0.0], theta: float=0.0) -> None:
        self.E = E
        self.r = r
        self.theta = theta

    def eval_xs(self, xs) -> Q_:
        """Evaluates a cross section at the neutron's energy  using log-log interpolation
        """
        for idx, (energy, sigma) in enumerate(zip(xs["energy"], xs["xs"])):
            if energy >= self.E:
                e1 = energy
                e2 = xs["energy"][idx + 1]
                s1 = sigma
                s2 = xs["xs"][idx + 1]
                break
        log_s1 = np.log(s1.m_as("barn"))
        log_s2 = np.log(s2.m_as("barn"))
        log_s_interp = ((e2.m_as("eV") - self.E.m_as("eV")) * log_s1 + (self.E.m_as("eV") - e1.m_as("eV")) * log_s2) / (e2.m_as("eV") - e1.m_as("eV"))
        s_interp = Q_(np.exp(log_s_interp), "barn")
        return s_interp

    def mean_free_path(self, material) -> Q_:
        """Returns the mean free path of the neutron in a material.
        """
        sigma_T = Q_(0, "cm**-1")
        for iso, dens in material.atom_densities.items():
            micro_xs = self.eval_xs(iso.get_xs("n", "total"))
            macro_xs = micro_xs * dens
            sigma_T += macro_xs
        return (1 / sigma_T).to("cm")

    def distance_to_next_collision(self, material) -> Q_:
        """Randomly samples the distance to the next collision.
        """
        return -np.log(1 - random.random()) * self.mean_free_path(material)

    def sample_nuclide_for_interaction(self, material) -> Isotope:
        """Samples the nuclide upon which an interaction will occur in a material.
        """
        # Quick exit for single-isotope materials
        if len(material.composition) == 1:
            return next(iter(material.composition.keys()))
        else:
            breakpoints = list()
            # Grab the total cross section for each constituent nuclide
            cdf = 0
            for iso, dens in material.atom_densities.items():
                macro_xs = self.eval_xs(iso.get_xs("n", "total")) * dens
                cdf += macro_xs.m_as("cm**-1")
                breakpoints.append([iso, cdf])
            rand = random.random()
            for bp in breakpoints:
                if bp[1] / cdf >= rand:
                    return bp[0]

    def sample_interaction_type(self, iso) -> str:
        """Samples the interaction type which occurs on a specific isotope.
        """
        possible_interactions = ["elastic_scatter", "capture"]
        if iso.element in ["U", "Pu"]:
            possible_interactions.append("fission")
        breakpoints = list()
        cdf = 0
        for interaction in possible_interactions:
            xs = self.eval_xs(iso.get_xs("n", interaction)).m_as("barn")
            cdf += xs
            breakpoints.append([interaction, cdf])
        rand = random.random()
        for bp in breakpoints:
            if bp[1] / cdf >= rand:
                return bp[0]

    def sample_next_interaction(self, material) -> Dict[str, Any]:
        """Sample the isotope upon which the next interaction will occur, as well as what type on interaction it is
        """
        next_iso = self.sample_nuclide_for_interaction(material)
        int_type = self.sample_interaction_type(next_iso)
        data = {
            "iso": next_iso,
            "interaction": int_type
        }
        return data

    def sample_scatter(self, iso: Isotope) -> Dict[str, Any]:
        """For a scatter off of a given isotope, returns an energy and angle of scatter.
        """
        A = iso.mass_number
        alpha = ((A - 1) / (A + 1)) ** 2
        rand = random.random()
        post_scatter_energy = self.E * (1 - (1 - alpha) * rand)
        scatter_angle = np.arccos(
            0.5 * ((A + 1) * np.sqrt(post_scatter_energy / self.E) - (A - 1) * np.sqrt(self.E / post_scatter_energy))
        )
        res = {
            "energy": post_scatter_energy,
            "scatter_angle": scatter_angle
        }