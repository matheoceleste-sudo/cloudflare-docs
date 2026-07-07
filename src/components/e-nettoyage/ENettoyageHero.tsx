import Hero from "~/components/ui/animated-shader-hero";

/**
 * Homepage hero for the e-Nettoyage demo site.
 *
 * Thin wrapper around the animated-shader-hero `Hero` so the CTA buttons
 * can carry `onClick` handlers (functions can't be passed from an Astro
 * page into a React island). The buttons smooth-scroll to the relevant
 * sections of the page.
 */
export default function ENettoyageHero() {
	const scrollTo = (id: string) => () => {
		document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
	};

	return (
		<Hero
			trustBadge={{
				text: "Plus de 2 000 foyers et bureaux nous font confiance",
				icons: ["✨"],
			}}
			headline={{
				line1: "Un espace impeccable,",
				line2: "sans lever le petit doigt",
			}}
			subtitle="e-Nettoyage réunit les meilleurs professionnels du ménage près de chez vous. Réservez en ligne en 2 minutes, payez en toute sécurité, et retrouvez un intérieur éclatant."
			buttons={{
				primary: {
					text: "Réserver un nettoyage",
					onClick: scrollTo("contact"),
				},
				secondary: {
					text: "Voir nos services",
					onClick: scrollTo("services"),
				},
			}}
		/>
	);
}
